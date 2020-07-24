from aws_cdk import core, aws_s3, aws_s3_deployment, aws_cloudfront, aws_route53, aws_route53_targets, aws_lambda, \
    aws_apigateway, aws_certificatemanager, aws_dynamodb
from aws_cdk.core import CfnOutput, RemovalPolicy

from aws_cdk.aws_cloudfront import AliasConfiguration, SourceConfiguration, CloudFrontWebDistribution

from secret_config import DOMAIN_WEBSITE


# from aws_cdk.aws_route53 import HostedZone

# CDK LAMBDA/CORS/APIGW BEISPIEL: https://github.com/aws-samples/aws-cdk-examples/blob/master/python/api-cors-lambda/app.py


class JukebikeStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # set variables for site s3 bucket
        bucket_name = DOMAIN_WEBSITE['bucket_name']
        website_index = DOMAIN_WEBSITE['website_index']
        website_error = DOMAIN_WEBSITE['website_error']
        website_code_folder = DOMAIN_WEBSITE['website_code_folder']
        site_domain = DOMAIN_WEBSITE['site_domain']
        certificate_domain = DOMAIN_WEBSITE['certificate_domain']
        api_domain = DOMAIN_WEBSITE['api_domain']
        hosted_zone_name = DOMAIN_WEBSITE['hosted_zone_name']
        hosted_zone_id = DOMAIN_WEBSITE['hosted_zone_id']

        #self.lambda_code = aws_lambda.Code.from_cfn_parameters()

        # retrieve hosted zone
        hosted_zone = aws_route53.HostedZone.from_hosted_zone_attributes(self, 'hostedZone',
                                                                         hosted_zone_id=hosted_zone_id,
                                                                         zone_name=hosted_zone_name)

        # set variables for backend
        lambda_code_location = "jukebike/backend/"

        # Construct code goes here
        CfnOutput(self, "Site", value=f"https://{site_domain}")

        # Content bucket
        site_bucket = aws_s3.Bucket(self, "websitebucket",
                                    bucket_name=bucket_name,
                                    website_index_document=website_index,
                                    website_error_document=website_error,
                                    public_read_access=True,
                                    removal_policy=RemovalPolicy.DESTROY)
        CfnOutput(self, "BucketArn", value=site_bucket.bucket_arn)
        CfnOutput(self, "WebsiteUrl", value=site_bucket.bucket_website_url)

        # Certificate
        cert = aws_certificatemanager.DnsValidatedCertificate(self, "certificate_website", domain_name=site_domain,
                                                              hosted_zone=hosted_zone, region="us-east-1")
        CfnOutput(self, 'CertificateArn', value=cert.certificate_arn)

        distr = CloudFrontWebDistribution(self, "SiteDistribution",
                                          alias_configuration=AliasConfiguration(
                                              acm_cert_ref=cert.certificate_arn,
                                              names=[site_domain],
                                              ssl_method=aws_cloudfront.SSLMethod.SNI,
                                              security_policy=aws_cloudfront.SecurityPolicyProtocol.TLS_V1_1_2016,
                                          ),
                                          origin_configs=[SourceConfiguration(
                                              s3_origin_source=aws_cloudfront.S3OriginConfig(
                                                  s3_bucket_source=site_bucket),
                                              behaviors=[aws_cloudfront.Behavior(is_default_behavior=True)]
                                          )])
        CfnOutput(self, "DistributionId", value=distr.distribution_id)
        #
        # Route 53 alias record for the cloudfront distribution
        aws_route53.ARecord(self, "SiteAliasRecord",
                            zone=hosted_zone,
                            target=aws_route53.AddressRecordTarget.from_alias(
                                aws_route53_targets.CloudFrontTarget(distr)),
                            record_name=site_domain)

        aws_s3_deployment.BucketDeployment(self, "DeployWithInvalidation",
                                           sources=[aws_s3_deployment.Source.asset(website_code_folder)],
                                           destination_bucket=site_bucket,
                                           distribution=distr,
                                           distribution_paths=["/*"]
                                           )

        ########################### Backend #################

        certificate = aws_certificatemanager.DnsValidatedCertificate(self, "domaincertificate", hosted_zone=hosted_zone,
                                                                     region='us-east-1', domain_name=certificate_domain,
                                                                     validation_method=aws_certificatemanager.ValidationMethod.DNS)

        ############# Search API ###################

        search_lambda = aws_lambda.Function(self, "SearchLambda",
                                                    code=aws_lambda.Code.from_asset(lambda_code_location),
                                                    handler="search.handler",
                                                    runtime=aws_lambda.Runtime.PYTHON_3_7
                                                    )

        CfnOutput(self, "SearchLambda_", value=search_lambda.function_arn)

        search_api = aws_apigateway.LambdaRestApi(
            self, 'SearchSpotifyEndpoint',
            handler=search_lambda,
        )


        ############# Whats-Next API ###################
        whats_next_lambda = aws_lambda.Function(self, "WhatsNextLambda",
                                                code=aws_lambda.Code.from_asset(lambda_code_location),
                                                handler="whats_next.handler",
                                                runtime=aws_lambda.Runtime.PYTHON_3_7
                                                )
        CfnOutput(self, "WhatsNextLambda_", value=whats_next_lambda.function_arn)

        whats_next_api = aws_apigateway.LambdaRestApi(
            self, 'WhatsNextEndpoint',
            handler=whats_next_lambda,
        )

        ############# Whats-Next API ###################
        wish_track_lambda = aws_lambda.Function(self, "WishTrackLambda",
                                                code=aws_lambda.Code.from_asset(lambda_code_location),
                                                handler="wish_track.handler",
                                                runtime=aws_lambda.Runtime.PYTHON_3_7
                                                )
        CfnOutput(self, "WishTrackLambda_", value=wish_track_lambda.function_arn)

        wish_track_api = aws_apigateway.LambdaRestApi(
            self, 'WishTrackEndpoint',
            handler=wish_track_lambda,
        )



        ################## Publish APIS with custom domain name ##############
        # Pre-Requirements:
        # [Manual] 1) Registered Domain with Route 53 (e.g. jacubasch.com)
        # 2) Certificate in North Virgina for domain (e.g. api.jacubasch.com) -> AWS Certification Manager
        # 3) API Gateway Custom Domain with Edge
        # 4) Alias-Record in Route53 forwarding to Cloudfront Target Domain Name (can be found in API Gateway)
        # TODO: in separaten Base-Stack auslagern?
        # https://medium.com/@maciejtreder/custom-domain-in-aws-api-gateway-a2b7feaf9c74

        domain = aws_apigateway.DomainName(self, 'searchDomain', certificate=certificate,
                                           endpoint_type=aws_apigateway.EndpointType.EDGE, domain_name=api_domain)
        domain.add_base_path_mapping(target_api=search_api, base_path="search")
        domain.add_base_path_mapping(target_api=whats_next_api, base_path="whats-next")
        domain.add_base_path_mapping(target_api=wish_track_api, base_path="wish-track")

        target = aws_route53_targets.ApiGatewayDomain(domain)
        record_target = aws_route53.RecordTarget.from_alias(target)
        alias_record = aws_route53.ARecord(self, 'aliasRecord', target=record_target, record_name=api_domain,
                                           zone=hosted_zone)

        CfnOutput(self, "AliasRecord_", value=alias_record.to_string())

        ################## Dynamo DB ##############

        # create dynamo table
        track_table = aws_dynamodb.Table(
            self, "track_table",
            partition_key=aws_dynamodb.Attribute(
                name="track_uri",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        # grant permission to lambda  & provide environment variable
        track_table.grant_write_data(wish_track_lambda)
        wish_track_lambda.add_environment("TRACK_TABLE_NAME", track_table.table_name)

        track_table.grant_read_write_data(whats_next_lambda)
        whats_next_lambda.add_environment("TRACK_TABLE_NAME", track_table.table_name)
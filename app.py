#!/usr/bin/env python3

from aws_cdk import core

from jukebike.jukebike_stack import JukebikeStack

from secret_config import AWS_ENV

#TODO: Prüfen für Javascript API GW Aufruf (Assets: Deploy time attributes example: https://docs.aws.amazon.com/cdk/latest/guide/assets.html )
# UND: Javascript SDK
# UND: https://stackoverflow.com/questions/60074546/aws-cdk-passing-api-gateway-url-to-static-site-in-same-stack
# https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/

#TODO: Optionen für Website-zu-Backend-Kommunikation: a) über Rest-Calls auf API Gateway (more losely coupled?) b) Javascript SDK auf Website



# Javascript Notizen
# jQuery: Bibliothek mit häufig genutzten Funktionen, um Code zu vereinfachen (z.B. AJAX)
# API Calls: gehen entweder direkt über Javascript mit Fetch (relativ neu) oder über JQuery Ajax
# JQuery Intro: https://www.w3schools.com/jquery/jquery_ajax_get_post.asp
# Arbeit mit Javascript Functions: https://www.w3schools.com/js/js_functions.asp
# Einbinden in Link: <a href="#" onClick="javascript:submitToAPI()">Privacy</a>
# CSS Tutorial: https://www.w3schools.com/css/default.asp
# JavaScript -> API Tutorial (without jQuery): https://www.taniarascia.com/how-to-connect-to-an-api-with-javascript/
# DOM Tutorial: https://www.digitalocean.com/community/tutorials/introduction-to-the-dom



#Steps for setup:
# mkdir jukebike
# cdk init app --lanuage python
# Pycharm: File Open => dann wird das projekt importiert
# prüfen, ob er virtual env verwendet
# dann evtl. pip install requirements.txt / oder "Tools" -> Run setup.py Task -> Install -> ok -> ok

#set account and region for environment

env_EU = core.Environment(account=AWS_ENV['ACCOUNT'], region=AWS_ENV['REGION'])

app = core.App()
jukebike_stack = JukebikeStack(app, "jukebike")

#PipelineStack(app, "PipelineDeployingLambdaStack",
#    lambda_code=jukebike_stack.lambda_code)
#PipelineStack2(app, "PipelineDeployStack")

app.synth()

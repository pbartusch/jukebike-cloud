# jukebike-cloud
#saveThePlanetWithMusic JukeBike cloud source code

# Instructions

How to get access token for Spotify API? (For Application without User Account Access)
https://developer.spotify.com/documentation/general/guides/authorization-guide/#client-credentials-flow
1. Log into Spotify Developer Account
2. Get User ID and Secret
3. Encode (base64) User and Secret in one String: "clientid:secret"
4. Get Token: curl -X "POST" -H "Authorization: Basic [put encoded key here]" -d grant_type=client_credentials https://accounts.spotify.com/api/token

How to use Search Functionality?
https://developer.spotify.com/console/get-search-item/?q=tania+bowra&type=artist

curl -X "GET" "https://api.spotify.com/v1/search?q=eminem%20stan&type=track&market=DE&limit=10&offset=0" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer <BEARER_TOKEN>"

# Welcome to your CDK Python project!

This is a blank project for Python development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

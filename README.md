Subscriptions
=============

App-engine project to display the static forms for the new Guardian
subscriptions.

It is currently available at
[http://guardian-subscriptions.appspot.com/](http://guardian-subscriptions.appspot.com/)

Usage
-----

* Download the google appengine sdk
* Create a virtualenv for the project
* Install jinja2 into the virtualenv

### Running the app locally

To run the app locally, use the following command.

    <path-to-virtualenv>/bin/python <path-to-google-appengine-sdk>/dev_appserver.py <path-to-subscriptions> --address 0.0.0.0

e.g.

    venv/bin/python ~/bin/google_appengine/dev_appserver.py . --address 0.0.0.0

### Deploying (uploading) your changes

Updating the application is done using the appcfg command in the
Python SDK.

    <path-to-virtualenv>/bin/python <path-to-google-appengine-sdk>/appcfg.py update <path-to-subscriptions>

e.g.

    venv/bin/python ~/bin/google_appengine/appcfg.py update .

Notes
-----

Subscriptions uses [pasteup](https://github.com/guardian/pasteup).

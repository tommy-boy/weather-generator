# weather-generator

=======
Weather Newsletter Generator
=======


###Description
* Weather Generator is developed to have ExactTarget access the app which will render the Weather Newsletter html file.
* Setup a local development environment (see Setup) and do a git pull Master.
* This should give you:
    
    ├── app
    ├── configs
    ├── .gitignore
    ├── install.txt
    ├── README.md
    ├── requirements.txt
    └── run.py



###Setup
* mkdir weathergenerator
* read install.txt



###Configuration
* configs/default.py holds the majority of the configs.
* default.py holds default configs.



###Developers
* tommmy boy
  # Feed Ingestion
  * tommy boy



###Versions
* WCG v2.0
  * Initial version of the app



###Deploying
* change the AP_ENV in __init__.py and in app.wsgi
* Add MONITOR_ID in configs default.py from flaskmonitor
* Adjust all the other variables in configs default.py
* Deploy both a staging environment and a production environment.
* adjust app.wsgi


from decouple import config

DEPLOY_MODE = config('DEPLOY_MODE')

if DEPLOY_MODE == 'dev':
    from .settings_dev import *
elif DEPLOY_MODE == 'production':
    from .settings_production import *

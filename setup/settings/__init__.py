from decouple import config

environment = config('DJANGO_ENV', default='local')

if environment == 'production':
    from .production import *
else:
    from .local import * 
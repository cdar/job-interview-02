# noinspection PyUnresolvedReferences
from .dev import *

import django_heroku

django_heroku.settings(locals())

# app doesn't work with postgres :/
# see README.txt
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

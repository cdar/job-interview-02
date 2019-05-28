# noinspection PyUnresolvedReferences
from .base import *

ROOT_URLCONF = 'secureaccesssite.urls.dev'

_p = os.path.abspath(__file__)
_p = os.path.dirname(_p)
_p = os.path.join(_p, '../../../media')
_p = os.path.normpath(_p)
MEDIA_ROOT = _p

django_heroku.settings(locals())

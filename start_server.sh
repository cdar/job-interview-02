#!/usr/bin/env bash

source ./venv/bin/activate
export DJANGO_SETTINGS_MODULE=secureaccesssite.settings.heroku
exec python ./secureaccesssite/manage.py runserver

#!/usr/bin/env bash

source ./venv/bin/activate
exec python ./secureaccesssite/manage.py runserver

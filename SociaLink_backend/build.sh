#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input --settings=SociaLink_backend.settingsprod

python manage.py migrate --settings=SociaLink_backend.settingsprod
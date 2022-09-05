#!/bin/sh

python manage.py collectstatic --no-input --clear

exec "$@"
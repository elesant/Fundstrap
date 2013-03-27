#!/bin/bash

git push git@heroku.com:fundstrap.git
heroku run python manage.py migrate --app fundstrap
heroku run python manage.py collectstatic --noinput --app fundstrap

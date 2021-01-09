#!/bin/bash

docker-compose run web ./manage.py createsuperuser --email=test@test.com --noinput
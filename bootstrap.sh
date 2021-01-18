#!/bin/bash

export FLASK_APP=index.py
export FLASK_ENV=development
export FLASK_RUN_PORT=5000
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0 #127.0.0.1
#!/bin/bash
mkdir db
pip install -r requirements.txt
python manage.py syncdb

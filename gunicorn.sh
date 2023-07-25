#!/bin/sh
gunicorn -c gunicorn.conf  -b 0.0.0.0:8080 -w 4 'app:create_app()' --logger-class=gunicorn_color.Logger --timeout 600 --keep-alive 600 --capture-output --log-level debug

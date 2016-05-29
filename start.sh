#!/bin/bash
#cp -r /home/box/stepic/web /home/box/
mv /home/box/stepic/ /home/box/web/
sudo ln -sf /media/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo nginx -t

#sudo ln -sf /media/sf_web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart﻿﻿
#gunicorn -c /etc/gunicorn.d/hello.py hello
cd /home/box/web
sudo gunicorn -b 0.0.0.0:8080 hello:app
cd ../web/ask
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000

#gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
#gunicorn -c /home/box/web/etc/django.py wsgi --daemon
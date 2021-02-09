#!/bin/bash
#cp -r /home/box/stepic/web /home/box/
sudo pip3 install django
sudo pip3 install gunicorn
mv /home/box/stepic/ /home/box/web/
sudo ln -sf /media/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo nginx -t


#sudo ln -sf /media/sf_web/etc/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
#gunicorn -c /etc/gunicorn.d/hello.py hello
#cd /home/box/web
#sudo gunicorn -b 0.0.0.0:8080 hello:app
#cd ../
#chmod -R 777 web/*
#cd web/ask
#gunicorn ask.wsgi:application --bind 0.0.0.0:8000 --daemon
#cd /home/box/web
#gunicorn -b 0.0.0.0:8080 hello:app --daemon

#gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
#gunicorn -c /home/box/web/etc/django.py wsgi --daemon
sudo ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
#sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
#cd /home/box/web
#gunicorn --bind 0.0.0.0:8000 ask.wsgi:application

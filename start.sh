#!/bin/bash
cp -r /home/box/stepic/web /home/box/
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo nginx -t
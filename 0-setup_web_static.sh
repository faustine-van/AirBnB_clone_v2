#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
apt-get update
apt-get -y install nginx

# create folder
mkdir -p /data/web_static/shared/
mkdir -p  /data/web_static/releases/test/

# create sysmbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change user user and group
chown -hR ubuntu:ubuntu /data/
# content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Update Nginx to serve the content of /data/web_static/current/ to hbnb_static
str="\\\tlocation {\n\t alias /data/web_static/current;\n\t}"
sed -i "62i $str" /etc/nginx/sites-available/default

# restart
service nginx restart

#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

# create folder
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p  /data/web_static/releases/test/

# create sysmbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# change user user and group
sudo chown -hR ubuntu:ubuntu /data/
# content
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Update Nginx to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "62i	location {\n\t alias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default

# restart
sudo service nginx restart

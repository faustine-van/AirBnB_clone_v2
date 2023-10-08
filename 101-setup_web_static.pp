# sets up your web servers for the deployment of web_static

exec {'Install nginx configure it and create data':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i "41i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf && sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/ && echo "Holberton School" > /data/web_static/releases/test/index.html && sudo ln -sf /data/web_static/releases/test/ /data/web_static/current && sudo chown -R ubuntu:ubuntu /data/ && sudo sed -i "42i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default && sudo service nginx restart && exit 0',
  provider => shell,
}

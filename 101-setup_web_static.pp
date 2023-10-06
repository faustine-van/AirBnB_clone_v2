# sets up your web servers for the deployment of web_static

package { 'nginx':
  ensure => 'present',
}
-> exec { 'create folder for file':
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
}

-> exec { 'create folder for shared':
  command  => 'sudo mkdir -p /data/web_static/shared/',
  provider => 'shell',
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Holberton School',
}

-> exec { 'create symbolic link':
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
}

-> exec { 'change owner':
  command  => 'sudo chown -hR ubuntu:ubuntu /data/',
  provider => 'shell',
}

-> exec { 'add to the server to serve content':
  command  => 'sudo sed -i "38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
  provider => 'shell',
}

-> exec { 'restart server':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}

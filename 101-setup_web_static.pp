# sets up your web servers for the deployment of web_static

package { 'nginx':
  ensure => 'present'
}
-> exec { 'create folder for file':
  command  => 'mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
}

-> exec { 'create folder for shared':
  command  => 'mkdir -p /data/web_static/shared/',
  provider => 'shell',
}
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Holberton School',
}

-> exec { 'create symbolic link':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
}

-> exec { 'change owner':
  command  => 'chown -hR ubuntu:ubuntu /data/',
  provider => 'shell',
}

-> exec { 'add to the server to serve content':
  command  => 'sed -i "51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default',
  provider => 'shell',
}

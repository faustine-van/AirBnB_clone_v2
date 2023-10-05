# sets up your web servers for the deployment of web_static

package { 'nginx':
  ensure => 'present',
}
-> file { '/data/web_static/releases/test/':
  ensure    => 'directory'
  recursive => true,
}

-> exec { '/data/web_static/shared/':
  ensure    => 'directory',
  resursive => true,
}
-> file { '/data/web_static/releases/test/index':
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

-> exec { 'restart server':
  command  => 'service nginx restart',
  provider => 'shell',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx configuration file is updated to handle more concurrent connections
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}

# Custom Nginx configuration template to increase worker_connections
# This is an example, you may need to adjust the values based on your server resources
# For production use, consider using a more optimized configuration
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
    worker_processes auto;
    worker_connections 1024;
    multi_accept on;
    use epoll;
    ...
    # Other Nginx configuration directives
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

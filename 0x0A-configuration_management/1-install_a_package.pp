# Use an exec resource to install flask from pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/bin',
  creates => 'usr/bin/flask',
}

# Use a package resource tp maanage the flask package
package { 'flask':
  ensure  => '2.1.0',
  require => Exec['install_flask'],
}

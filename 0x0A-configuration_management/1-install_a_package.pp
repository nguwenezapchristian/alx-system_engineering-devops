# install flask from pip3

exec{ 'apt-get-update':
  command => 'usr/bin/apt-get update',
}

exec{ 'install-python3-pip':
  command => 'usr/bin/apt-get install -y python3-pip',
  require => Exec['apt-get-update'],
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install-python3-pip'],
}

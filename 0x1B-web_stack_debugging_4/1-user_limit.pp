# Increase user limits for the holberton user

# Define the limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192",
}

# Apply the new limits for the holberton user
exec { 'apply_user_limits':
  command     => 'sysctl -p',
  refreshonly => true,
}

# Set the proper ownership and permissions for the configuration file
file { '/etc/security/limits.d/holberton.conf':
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Exec['apply_user_limits'],
}

# Using Puppet, create a manifest that kills a process named killmenow
exec { 'kills-process':
  command => '/usr/bin/pkill killmenow'
}

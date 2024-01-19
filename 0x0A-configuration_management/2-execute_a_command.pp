# Using Puppet, create a manifest that kills a process named killmenow
exec { 'kills-process':
  command => 'pkill killmenow'
}

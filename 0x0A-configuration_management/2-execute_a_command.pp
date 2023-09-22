# Executing a command
Exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}

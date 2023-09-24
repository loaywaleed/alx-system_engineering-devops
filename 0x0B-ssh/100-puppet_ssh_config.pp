# puppet config file
file_line { 'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
file_line { 'disable password auth':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}


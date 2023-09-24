# puppet config file
file_line {'disable password auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no'
}
file_line {'IdentityFile':
  ensure => 'present'
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}

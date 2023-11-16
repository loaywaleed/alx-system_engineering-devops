# Handling high requests

exec {'replace limit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'reboot':
  provider => shell,
  command  => 'sudo service nginx restart',
}

# Change the OS configuration enabling  login with the `holberton` user and opening a file without any error message

exec { 'set_hard_ulimit':
  command => "sed -i '/^holberton\\s*hard\\s*nofile/s/.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}


exec { 'set_soft_ulimit':
  command => "sed -i '/^holberton\\s*soft\\s*nofile/s/.*/holberton soft nofile 4096/' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}

# A puppet manifest to change the limit of files to be opened by the webserver

exec { 'set_ulimit':
  command => 'sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/g\' /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}


# A Puppet manifiest to create a custom HTTP header response, but with Puppet.

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

# Update config file with custom header
file_line {'add_custom_header':
  ensure  => present,
  line    => "\tserver_name _;\n\tadd_header X-Served-By 127.0.0.1;",
  match   => 'server_name _;',
  path    => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

exec {'restart':
  command => '/usr/sbin/service nginx restart',
}

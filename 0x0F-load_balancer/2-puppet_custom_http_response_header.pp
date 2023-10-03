# A Puppet manifiest to create a custom HTTP header response, but with Puppet.

exec {'update':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => installed,
  require => Exec['update'],
}

$custom_header= 'add_header X-Served-By "$localhost";'
$config_file= '/etc/nginx/sites-available/default'

# Read the content of the file
# $config_content = file($config_file)

$search_str= 'server_name _;'
$replacement_str = 'server_name _;\n\tadd_header X-Served-By "$hostname";'

# Use of the replace fucntion to modify the content of the config file
# $modified_cont = replace($config_content, $search_str, $replacement_str)

# Update config file with custom header

file_line {'add_custom_header':
  ensure  => present,
  line    => $replacement_str,
  match   => $search_str,
  path    => $config_file,
  require => Package['nginx'],
}

exec {'restart':
  command => '/usr/bin/service nginx restart',
  require => File[$config_file],
}

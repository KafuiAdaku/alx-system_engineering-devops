# Replaces a line in the specified file
exec { 'fix_wp_settings':
  command => 'sed -i "s/\.phpp/\.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/bin:/bin',
}

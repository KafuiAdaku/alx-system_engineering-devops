# A manifest that makes changes to an ssh client configuration file
file {'/root/.ssh/config':
    ensure  => 'present',
    content => @(EOT)
        HOST alx-server
        HostName 100.24.205.66
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    EOT
}

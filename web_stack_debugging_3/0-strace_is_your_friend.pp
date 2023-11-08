# fixing .phpp extensions to .php
exec { 'debugging_lamp':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/bin/'
}

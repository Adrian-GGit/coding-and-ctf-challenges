<?php
define('DB_SERVER', '127.0.0.1');
define('DB_USERNAME', 'user');
define('DB_PASSWORD', 'VerySafePassword1337');
define('DB_NAME', 'greetingsplatform');

$SITE_NAME = "Greetings";

try {
    $database_connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME, 3306);
} catch(Exception $e) {
    $database_connection = false;
}

if($database_connection === false){
    //die("ERROR: Could not connect. " . mysqli_connect_error());
    exit;
}


?>

<?php
// Config for db connection
$host = 'localhost';
$dbName = "api";
$dbUser = 'root';
$dbPassword = '';

try{
    $pdo =new PDO('mysql:host='.$host.';mysql:dbname='.$dbName.'; charset=utf8', $dbUser, $dbPassword);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(Exception $e){
    die('Error connection: '.$e->getMessage());
}
?>
<?php
require 'vendor/autoload.php';

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

$app->get('/chambre/{4}', function (Request $request, Response $response) {
    $id = $request->getAttribute('4');
    return getChambre($id);
});
function connexion()
{
    return $dbh = new PDO("mysql:host=localhost;dbname=finder", 'root', '', array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'));
}
function getChambre($id)
{
    $sql = "SELECT * FROM chambre";
    try {
        $dbh = connexion();
        $statement = $dbh->prepare($sql);
        $statement->execute();
        $result = $statement->fetchAll(PDO::FETCH_CLASS);
        return json_encode($result, JSON_PRETTY_PRINT);
    } catch (PDOException $e) {
        return '{"error":' . $e->getMessage() . '}';
    }
}

<?php 
require 'vendor/autoload.php';
use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Response;

$app = new \Slim\App;
$app->get('/zaza', function(Request $request, Response $response){	
	return "wazaaaaaaaa";
});






$app->get('/chambres', function(Request $request, Response $response){
       return getChambres();
});



$app->get('/chambre/{id}', function(Request $request, Response $response){
	$id = $request->getAttribute('id');
       return getChambre($id);
});
$app->get('/disponibilites', function(Request $request, Response $response){
   $tb = $request->getQueryParams();
    $cat = $tb["cat"];
    $dd = $tb["dated"];
    $df = $tb["datef"];
  return getDispos($cat, $dd,$df);
});








$app->run();


function connexion()
{
    return $dbh = new PDO("mysql:host=localhost;dbname=hotela", 'zaza', 'zaza', array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'));
}
function getChambre($id)
{
	$sql = "SELECT * FROM chambre where id='$id'";
	try{
		$dbh=connexion();
		$statement = $dbh->prepare($sql);
		$statement->execute();
		 $result = $statement->fetchAll(PDO::FETCH_CLASS); 
                 return json_encode($result, JSON_PRETTY_PRINT);
	} catch(PDOException $e){
		return '{"error":'.$e->getMessage().'}';
	}
}
function getChambres()
{
	$sql = "SELECT * FROM chambre";
	try{
		$dbh=connexion();
		$statement = $dbh->prepare($sql);
		$statement->execute();
		 $result = $statement->fetchAll(PDO::FETCH_CLASS); 
                 return json_encode($result, JSON_PRETTY_PRINT);
	} catch(PDOException $e){
		return '{"error":'.$e->getMessage().'}';
	}
}
function getDispos($cat, $dd,$df)
{
 $sql ="select * from chambre where idCategorie=(select id from categorie where libelle='$cat')
and chambre.id not in( SELECT chambre.id FROM chambre inner join ligne_reservation on chambre.id=ligne_reservation.idchambre inner join reservation on  reservation.id=ligne_reservation.idreservation where reservation.dateD>='$df' or reservation.dateF<='$dd' )";
  try{
    $dbh=connexion();
    $statement = $dbh->prepare($sql);
    $statement->execute();
     $result = $statement->fetchAll(PDO::FETCH_CLASS); 
                 return json_encode($result, JSON_PRETTY_PRINT);
  } catch(PDOException $e){
    return '{"error":'.$e->getMessage().'}';
}
}


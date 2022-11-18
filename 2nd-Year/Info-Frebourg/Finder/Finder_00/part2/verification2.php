<?php session_start();

if(
   isset($_GET['email']) 
&& isset($_GET['password'])
){
   //echo "ok";
   $dsn='mysql:dbname=erambq;host=localhost';
$user='root';
$password='root';
try{
    $dbh=new PDO($dsn,$user,$password); 
}catch(PDOException $e){
    echo'Connexion échouée:'.$e->getMessage(); 
}
   $sql = "SELECT count(*) FROM finder_user WHERE Finder_email=:email 
   AND Finder_password=:password";
   //echo $sql;
   $resultats = $dbh->prepare($sql);
   $email = $_GET['email'];
   $password = $_GET['password'];
   $resultats->bindParam(":email", $email);
   $resultats->bindParam(":password", $password);
   $resultats->execute();  
   $number_of_rows = $resultats->fetchColumn(); 
   //echo $number_of_rows;

   if($number_of_rows == 1){
      http_response_code(200);
   }
   else{
      http_response_code(403);
    //$_SESSION['erreur']=true;
    //header('Location: http://localhost/finder1/connexion.php');
   }
}else{
   http_response_code(403);
        //$_SESSION['erreur']=true;
        //header('Location: http://localhost/finder1/connexion.php');
}
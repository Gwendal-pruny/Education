<?php

if (
   isset($_GET['email'])
   && isset($_GET['password'])
) {
   //echo "ok";
   $dsn = 'mysql:dbname=finder;host=localhost:3306';
   $user = 'root';
   $password = '';
   try {
      $dbh = new PDO($dsn, $user, $password);
   } catch (PDOException $e) {
      echo 'Connexion échouée:' . $e->getMessage();
   }
   $sql = "SELECT count(*) FROM user1 WHERE email=:email 
   AND password=PASSWORD(:password)";
   //echo $sql;
   $resultats = $dbh->prepare($sql);
   $email = $_GET['email'];
   $password = $_GET['password'];
   $resultats->bindParam(":email", $email);
   $resultats->bindParam(":password", $password);
   $resultats->execute();
   $number_of_rows = $resultats->fetchColumn();
   //echo $number_of_rows;

   if ($number_of_rows == 1) {
      echo "ok";
   } else {
      $_SESSION['erreur'] = true;
      header('Location: http://localhost/Finder\Finder\Finder_00\part1\connexion.html');
   }
} else {
   $_SESSION['erreur'] = true;
   header('Location: http://localhost/Finder\Finder\Finder_00\part1\connexion.html');
}

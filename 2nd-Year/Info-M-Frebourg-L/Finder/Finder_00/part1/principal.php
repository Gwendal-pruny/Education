<html>
    <head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
    </head>
    <body style='background:#fff;'>
        <div id="content">
            <?php
            session_start();
            if($_SESSION['username'] !== ""){
                $user = $_SESSION['username'];
                echo "Bonjour $user, vous êtes connecté";
            }
            ?>
        
            <a href='principal.php?deconnexion=true'><span>Déconnexion</span></a>
 
            <!-- tester si l'utilisateur est connecté -->
            <?php
            if(isset($_GET['deconnexion']))
            { 
                if($_GET['deconnexion']==true)
                { 
                    session_unset();
                    header("location:connexion.html");
                }
            }
            // else if($_SESSION['username'] !== ""){
            //     $user = $_SESSION['username'];
            //     // afficher un message
            //     echo "<br>Bonjour $user, vous êtes connectés";
            // }
            ?>
        </div>

    </body>
</html>
$(document).ready(function () {
    //click sur l'id btn
        $('#btn').click(function () {
            $.ajax("http://localhost/Finder/part2/index.php",//appel de index.php sur le serveur web
                {
                    type: "GET",
                    success: function (resultat) {
                        $("#result").html(resultat);
                    }
                });
        });
    });
var express = require('express');
var cors= require('cors');
var hostname = 'localhost'; 
var port = 8080; 
var app = express(); 
app.use(cors());
app.get('/bonjour', function(req, res){ 
    res.json({message : "Youhou", methode : req.method});
})
// Démarrer le serveur 
app.listen(port, hostname, function(){
  console.log("Mon serveur fonctionne sur http://"+ hostname +":"+port); 
});
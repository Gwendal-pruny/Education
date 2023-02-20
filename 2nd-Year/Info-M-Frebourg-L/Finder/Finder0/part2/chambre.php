<?php
    session_start();
    include('dbcon.php');
 
    if (!isset($_SESSION['user']) ||(trim ($_SESSION['user']) == '')){
        header('location:index.php');
    }
 
    $sql="select * from vueuser where id='".$_SESSION['user']."'";
    $query=$conn->query($sql);
    $row=$query->fetch_array();
 
?>
<!DOCTYPE html>
<html>
<head>
    <title>Vue.js Axios Login with PHP MySQLi</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link href="style.css" media="screen" type="text/css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="jumbotron">
            <h1 class="text-center">Welcome, <?php echo $row['username']; ?>!</h1>
            <a href="logout.php" class="btn btn-primary"><span class="glyphicon glyphicon-log-out"></span> Logout</a>
        </div>
    </div>
    <div id="app">
            <h1><span class="blue">&lt;</span>Table<span class="blue">&gt;</span> <span class="yellow">Responsive</pan></h1>
            <h2>Created with love by <a href="https://github.com/Zerio113" target="_blank">Gwendal Pruny</a></h2>
            
            <p>Faire une recherche parmis les hôtel:</p>
            <div class="input-group mb-3">
                <input v-model="idc" type="text" class="form-control" placeholder="Numéro de chambre" aria-label="Numéro de chambre" aria-describedby="button-addon2">
                <button v-on:click="ajax(idc)" class="btn btn-outline-secondary btn-dark" type="button" id="button-addon2"><span class="glyphicon glyphicon-check"></span>Valider</button>
            </div>
            
            <table class="container">
                <thead>
                    <tr>
                        <th><h1>Id</h1></th>
                        <th><h1>Prix de base</h1></th>
                        <th><h1>Nombre de Couchage</h1></th>
                        <th><h1>Etage</h1></th>
                        <th><h1>Porte</h1></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in info">
                        <td>{{ item.id }}</td>
                        <td>{{ item.prixBase }}</td>
                        <td>{{ item.nbCouchage }}</td>
                        <td>{{ item.etage }}</td>
                        <td>{{ item.porte }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <script>
        new Vue({
            el: '#app',
            data () {
                return {
                info: null,
                idc: null,
                message:''
                }
            },
            mounted () {
                axios({
                    method: 'get',
                    url: '/api/index.php/chambres',
                    responseType: 'json',
                })
                .then(async res => { 
                    if(res.status === 200) { 
                        alert('Ok voici les chambres!');
                        this.info=res.data;
                        console.log(res);
                    } else if(res.status === 400) { 
                        alert('Bad!');
                        let errorResponse = await res.json(); this.errors.push(errorResponse.error); }
                });
            },
            methods: {
                ajax: function (idc, event) {
                    axios({
                        method: 'get',
                        url: '/api/index.php/chambre/'+idc,
                        responseType: 'json',    
                    })
                    .then(async res => { 
                        if(res.status === 200) { 
                            alert('Ok!');
                            this.info=res.data;                     
                        } else if(res.status === 400) { 
                            let errorResponse = await res.json(); this.errors.push(errorResponse.error); }
                    })  
                }
            }
        })
    </script>
</body>
</html>
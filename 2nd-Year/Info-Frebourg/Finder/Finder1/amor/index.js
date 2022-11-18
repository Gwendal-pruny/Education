$( document ).ready(function() {

    $('#btn-new-liste').click(function(){ 
      let idx=$('#idx').val();
        $.ajax({ 
        type: "GET",
        url: "http://localhost.=/finder/finder/finder1/amor/index.php"+idx,
        success: function(data){  
          $("#result").html(data);
        }
      });
    });
   });
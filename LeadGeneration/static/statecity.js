$(document).ready(function(){
    $.getJSON("http://localhost:8000/api/statelist",function(data){
     
        data.map((item)=>{
        $('#inputState').append($('<option>').text(item.statename).val(item.stateid))

        }) 
     
    })
$('#inputState').change(function(){

    $.getJSON("http://localhost:8000/api/citylist",{"stateid":$('#inputState').val()},function(data){
    $('#inputCity').empty()
    $('#inputCity').append($('<option>').text('Choose City...'))
    data.map((item)=>{
    $('#inputCity').append($('<option>').text(item.cityname).val(item.cityid))

    }) 
 
})
   


}) 

})
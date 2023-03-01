$(document).ready(function(){

    $.getJSON("http://localhost:8000/api/managerlist",function(data){
     
    data.map((item)=>{
    $('#managerid').append($('<option>').text(item.firstname+" "+item.lastname).val(item.id))

    }) 
 
})
})
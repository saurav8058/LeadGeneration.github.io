const inputs = document.querySelectorAll(".input");
  
  
  function addcl(){
	  let parent = this.parentNode.parentNode;
	  parent.classList.add("focus");
  }
  
  function remcl(){
	  let parent = this.parentNode.parentNode;
	  if(this.value == ""){
		  parent.classList.remove("focus");
	  }
  }
  
  
  inputs.forEach(input => {
	  input.addEventListener("focus", addcl);
	  input.addEventListener("blur", remcl);
  });




  $(document).ready(function(){
   var status='1'
   var pagelink='admindashboard'   
  $('.btnl').click(function(){
     
    $(".btnl").map((i,item)=>{
     
      if($(this).attr('status')==$(item).attr('status'))
      {
         $(this).css('background', 'linear-gradient(to right, #32be8f, #38d39f, #32be8f)')
        status=$(this).attr('status')           
        pagelink=$(this).attr('pagelink') 
      }
      else{
          $(item).css('background','#d63031')
      }
    })  
  })
 $('#login').click(function(){
   if(status==1) 
  { $.getJSON('/api/checkadminlogin',{mobileno:$('#mobileno').val(),password:$('#password').val()},
  function(data){
   if(data.status)
   {
      window.location.href=`http://localhost:8000/api/admindashboard`
   }
   else
   {alert("Invalid Admin  Mobileno/Password")}

  })
 
  }
  else  if(status==2) 
  { $.getJSON('/api/checkmanagerlogin',{mobileno:$('#mobileno').val(),password:$('#password').val()},
  function(data){
   if(data.status)
   {
      window.location.href=`http://localhost:8000/api/managerdashboard`
   }
   else
   {alert("Invalid Admin  Mobileno/Password")}

  })
 
  }
  else  if(status==3) 
  { $.getJSON('/api/checkemployeelogin',{mobileno:$('#mobileno').val(),password:$('#password').val()},
  function(data){
   if(data.status)
   {
      window.location.href=`http://localhost:8000/api/employeedashboard`
   }
   else
   {alert("Invalid Admin  Mobileno/Password")}

  })
 
  }
 })
  })
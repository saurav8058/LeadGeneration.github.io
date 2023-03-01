from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from . import tuple_to_dict
from django.shortcuts import redirect


from django.views.decorators.clickjacking import xframe_options_exempt


from LeadManagementApp.models import Manager
from LeadManagementApp.serializers import ManagerSerializer
from django.http.response import JsonResponse


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerInterface(request):
    return render(request,"Manager.html",{})
 
@xframe_options_exempt
def DisplayAllManager(request):
    return render(request,"DisplayAllManager.html",{})

 
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
   if request.method == 'POST':
   
      manager_serializer = ManagerSerializer(data=request.data)
      if manager_serializer.is_valid():
          manager_serializer.save()
          return render(request,"Manager.html",{"message":"Record Submitted Successfully"})
     
      
      return render(request,"Manager.html",{"message":"Fail to Submit Record"})
    
'''
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
  if request.method=='GET':
    manager_list=Manager.objects.all()
    manager_serializer=ManagerSerializer(manager_list,many=True)
    #print("Employee",employee_serializer.data)
    return JsonResponse(manager_serializer.data,safe=False)
  return JsonResponse({},safe=False)
'''
 
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select M.*,(select S.statename from leadmanagementapp_states S where S.stateid=M.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=M.city) as cityname from leadmanagementapp_manager M"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
  
   return JsonResponse({},safe=False)

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_List_By_ID(request):
   if request.method=='GET':
    managerid=request.GET['managerid']
    cursor=connection.cursor()
    q="select M.*,(select S.statename from leadmanagementapp_states S where S.stateid=M.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=M.city) as cityname from leadmanagementapp_manager M where M.id={0}".format(managerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])

    if(data['gender']=='Male'):mg=True 
    else:mg=False
    
    if(data['gender']=='Female'):fg=True 
    else:fg=False
    
    return render(request,"ManagerBYID.html",{'record':data,'mgender':mg,'fgender':fg})
  
   return JsonResponse({},safe=False)  


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       manager=Manager.objects.get(pk=request.GET['id']) 
       manager.firstname=request.GET['firstname']
       manager.lastname=request.GET['lastname']
       manager.dob=request.GET['dob']
       manager.emailid=request.GET['emailid']
       manager.mobileno=request.GET['mobileno']
      
       manager.address=request.GET['address']
       manager.state=request.GET['state']
       manager.city=request.GET['city']
      
      

       manager.save()
      else:
        manager=Manager.objects.get(pk=request.GET['id']) 
        manager.delete()  
   return redirect('/api/displayallmanager')
''' 
@api_view(['GET', 'POST', 'DELETE'])
def Manager_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadmanagementapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadmanagementapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadmanagementapp_manager M where M.id=E.managerid) as mlastname from leadmanagementapp_employee E"
    cursor.execute(q)
    managerrecords=cursor.fetchall()
    description=cursor.description
    columnnames=[]
    for des in description:
       columnnames.append(des[0])
    data=[]
    for row in managerrecords:
      data.append(dict(zip(columnnames,list(row))))
    return JsonResponse(data,safe=False)
  
   return JsonResponse({},safe=False) 
'''
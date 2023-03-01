
from django.db import connection
from django.views.decorators.clickjacking import xframe_options_exempt



from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .import tuple_to_dict


from LeadManagementApp.models import Employee
from LeadManagementApp.models import States
from LeadManagementApp.models import Cities
from LeadManagementApp.serializers import StatesSerializer
from LeadManagementApp.serializers import CitiesSerializer
from LeadManagementApp.serializers import EmployeeSerializer

from django.http.response import JsonResponse
from django.shortcuts import redirect

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def EmployeeInterface(request):
    return render(request,"Employee.html",{})
 
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employeedash(request):
    return render(request,"employeedash.html",{})
 
@xframe_options_exempt 
def DisplayAllEmployee(request):
    return render(request,"DisplayAllEmployee.html",{})  
  

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def EmployeeSubmit(request):
  
  if request.method == 'POST':
 
    # employee_data = request.GET.dict()
    #print("Employeeeeeeeeeeeee",request.data)
    employee_serializer = EmployeeSerializer(data=request.data)
    if employee_serializer.is_valid():
        employee_serializer.save()
        return render(request,"Employee.html",{"message":"Record Submitted Successfully"})

  return render(request,"Employee.html",{"message":"Server Error:Fail to Submit Record"})
'''
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List(request):
   if request.method=='GET':
    #employee_list=Employee.objects.all()
    employee_list=Employee.objects.raw('select E.* from leadmanagementapp_employee E')  
    employee_serializer=EmployeeSerializer(employee_list,many=True)
    return JsonResponse(employee_serializer.data,safe=False)
   return JsonResponse({},safe=False) 
'''
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadmanagementapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadmanagementapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadmanagementapp_manager M where M.id=E.managerid) as mlastname from leadmanagementapp_employee E"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
  
   return JsonResponse({},safe=False)   
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List_By_Id(request):
   if request.method=='GET':
    employeeid=request.GET['employeeid']
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadmanagementapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadmanagementapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadmanagementapp_manager M where M.id=E.managerid) as mlastname from leadmanagementapp_employee E where E.id={0}".format(employeeid)
    
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])

    if(data['gender']=='Male'):mg=True 
    else:mg=False
    
    if(data['gender']=='Female'):fg=True 
    else:fg=False
    
    return render(request,"EmployeeById.html",{'record':data,'mgender':mg,'fgender':fg})
  
   return JsonResponse({},safe=False)  

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def State_List(request):
   if request.method=='GET':
    state_list=States.objects.all() 
    
    state_serializer = StatesSerializer(state_list,many=True)
    
    return JsonResponse(state_serializer.data,safe=False)
   return JsonResponse({},safe=False) 

@xframe_options_exempt 
@api_view(['GET', 'POST', 'DELETE'])
def City_List(request):
   if request.method=='GET':
    city_list=Cities.objects.raw("select * from leadmanagementapp_cities where stateid={0}".format(request.GET['stateid']))
    
    city_serializer = CitiesSerializer(city_list,many=True)
    
    return JsonResponse(city_serializer.data,safe=False)
   return JsonResponse({},safe=False) 

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       employee=Employee.objects.get(pk=request.GET['id']) 
       employee.firstname=request.GET['firstname']
       employee.lastname=request.GET['lastname']
       employee.dob=request.GET['dob']
       employee.gender=request.GET['gender']
       employee.emailid=request.GET['emailid']
       employee.mobileno=request.GET['mobileno']
       employee.address=request.GET['address']
       employee.state=request.GET['state']
       employee.city=request.GET['city']
       employee.designation=request.GET['designation']
       employee.managerid=request.GET['managerid']

       employee.save()
      else:
        employee=Employee.objects.get(pk=request.GET['id']) 
        employee.delete()  
   return redirect('/api/displayallemployee')

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_Display_Picture(request):
   if request.method=='GET':
      return render(request,"EmployeePicture.html",{"id":request.GET['employeeid'],"employeename":request.GET['employeename'],'picture':request.GET['picture']})

@xframe_options_exempt     
@api_view(['GET', 'POST', 'DELETE'])
def UpdateEmployeeImage(request):
  
  if request.method == 'POST':
     employee=Employee.objects.get(pk=request.POST['id']) 
     employee.photograph=request.FILES['photograph']
     employee.save()
  return redirect('/api/displayallemployee') 
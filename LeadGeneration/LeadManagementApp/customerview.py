from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse
from django.shortcuts import redirect

from django.views.decorators.clickjacking import xframe_options_exempt

from LeadManagementApp.serializers import StatesSerializer
from LeadManagementApp.serializers import CitiesSerializer
from LeadManagementApp.serializers import CustomerSerializer
from LeadManagementApp.models import States
from LeadManagementApp.models import Cities
from LeadManagementApp.models import Customer
from . import tuple_to_dict


from django.db import connection

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerInterface(request):
    return render(request,"Customer.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CustomerSubmit(request):
    if request.method == 'POST':
        customer_serializer = CustomerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return render(request,"Customer.html",{"message":"Record Submitted Successfully"})
        return render(request,"Customer.html",{"message":"Fail to Submit Record"})
    
    
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def DisplayAllCustomer(request):
    return render(request,"DisplayAllCustomer.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List(request):
   if request.method == 'GET':
    cursor=connection.cursor() 
    q="select u.*,(select S.statename from leadmanagementapp_states S where S.stateid=u.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=u.city) as cityname from leadmanagementapp_customer u"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
  
   return JsonResponse({},safe=False) 

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List_By_Id(request):
   if request.method=='GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor()
    q="select u.*,(select S.statename from leadmanagementapp_states S where S.stateid=u.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=u.city) as cityname from leadmanagementapp_customer u where u.id={0}".format(customerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])
    return render(request,"CustomerById.html",{'record':data})
  
   return JsonResponse({},safe=False)



@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       customer=Customer.objects.get(pk=request.GET['id']) 
       customer.firstname=request.GET['firstname']
       customer.lastname=request.GET['lastname']
       customer.dob=request.GET['dob']
       customer.emailid=request.GET['emailid']
       customer.mobileno=request.GET['mobileno']
       customer.alternateno=request.GET['alternateno']
       customer.address=request.GET['address']
       customer.state=request.GET['state']
       customer.city=request.GET['city']
       customer.organizationname=request.GET['organizationname']
      

       customer.save()
      else:
        customer=Customer.objects.get(pk=request.GET['id']) 
        customer.delete()  
   return redirect('/api/displayallcustomer')
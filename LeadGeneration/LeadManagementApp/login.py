from django.db import connection


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from .import tuple_to_dict
from django.http.response import JsonResponse
# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def Login(request):
    return render(request,"Login.html",{})
def AdminDashboard(request):
   try: 
    admin=request.session['ADMIN']
    print("Session:",admin)
    return render(request,"AdminDashboard.html",{'admin':admin})
   except:
    return render(request,"Login.html",{})  
def ManagerDashboard(request):
    return render(request,"ManagerDashboard.html",{})
def EmployeeDashboard(request):
    return render(request,"EmployeeDashboard.html",{})        

@api_view(['GET', 'POST', 'DELETE'])
def Check_Admin_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadmanagementapp_administrator where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
     print("ADMIN DATA:",data)   
     request.session['ADMIN']=data
     return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   


   return JsonResponse({},safe=False)
@api_view(['GET', 'POST', 'DELETE'])
def Check_Manager_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadmanagementapp_manager where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
     return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   


   return JsonResponse({},safe=False)
@api_view(['GET', 'POST', 'DELETE'])
def Check_Employee_Login(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select * from leadmanagementapp_employee where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    if(len(data)==1):
     return JsonResponse({"data":data,"status":True},safe=False)
    else:
     return JsonResponse({"data":{},"status":False},safe=False)   


   return JsonResponse({},safe=False)
@api_view(['GET', 'POST', 'DELETE'])
def LogoutAdmin(request):
    del request.session['ADMIN']
    return render(request,"Login.html",{})

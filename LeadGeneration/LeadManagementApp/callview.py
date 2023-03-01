from django.db import connection

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser



from LeadManagementApp.serializers import CallDetail
from LeadManagementApp.serializers  import CallSerializer
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt





@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CallDetailSubmit(request):
    if request.method == 'POST':
       
        print("calldetail:",request.data)
        call_serializer = CallSerializer(data=request.data)
        if call_serializer.is_valid():
            call_serializer.save()
            return render(request, "CallDetail.html", {"message": "Record Submitted Successfully"})

        return render(request, "CallDetail.html", {"message": "Fail to Submit Record"})

    
    
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def FillDetail(request):
    print('hello',FillDetail)
    return render(request,"Displayfilldetail.html",{})

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Caller_List(request):
    if request.method == 'GET':
        caller_list = CallDetail.objects.raw('select * from leadmanagementapp_calldetail')
        call_serializer = CallSerializer(caller_list, many=True)
        
        return JsonResponse(call_serializer.data, safe=False)
        
    return JsonResponse({}, safe=False)

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Caller_List_By_Id(request):
   if request.method=='GET':
    calldetailid=request.GET['calldetailid']
    cursor=connection.cursor()
    q="select L.* from leadmanagementapp_calldetail L where L.id={0}".format(calldetailid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['currentdate']=str(data['currentdate'])
    return render(request,"callerlistbyid.html",{'record':data})
  
   return JsonResponse({},safe=False)

  
   

  
 
    
    

@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Caller_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       callDetail=CallDetail.objects.get(pk=request.GET['id']) 
       callDetail.currentdate=request.GET['currentdate']
       callDetail.phonestatus=request.GET['phonestatus']
       callDetail.conversation=request.GET['conversation']
       callDetail.leadstatus=request.GET['leadstatus']
       
       callDetail.save()
      else:
        callDetail=CallDetail.objects.get(pk=request.GET['id']) 
        callDetail.delete()  
   return redirect('/api/displayfilldetail')




@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Customer_List_By_Id(request):
   if request.method=='GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor()
    q="select Cu.*,(select S.statename from leadmanagementapp_states S where S.stateid=Cu.state) as statename,(select C.cityname from leadmanagementapp_cities C where C.cityid=Cu.city) as cityname from leadmanagementapp_customer Cu where Cu.id={0}".format(customerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])
    print("Customer:",data)
    
    keys=list(request.session.keys())
    print("SESSION:",keys,request.session['ADMIN'])
    user={'caller':keys[0]}
    if("ADMIN" in keys):
        user['id']=request.session['ADMIN'][0]['id']
        user['name']=request.session['ADMIN'][0]['adminname']
    elif("MANAGER" in keys):
        user['id']=request.session['MANAGER'][0]['id']
        user['name']=request.session['MANAGER'][0]['firstname']+" "+request.session['MANAGER'][0]['lastname']    
    elif("EMPLOYEE" in keys):
        user['id']=request.session['EMPLOYEE'][0]['id']
        user['name']=request.session['EMPLOYEE'][0]['firstname']+" "+request.session['EMPLOYEE'][0]['lastname']    





    return render(request,"CallDetail.html",{'record':data,'user':user})
  
   return JsonResponse({},safe=False)

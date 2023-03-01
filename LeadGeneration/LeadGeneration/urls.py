"""LeadGeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import admin

from django.urls import include, re_path
from LeadManagementApp import views
from LeadManagementApp import managerview
from LeadManagementApp import customerview
from LeadManagementApp import login
from LeadManagementApp import callview



urlpatterns = [
    re_path('admin/', admin.site.urls),
    
   
    re_path(r'^api/employeeinterface', views.EmployeeInterface),
    re_path(r'^api/displayallemployee', views.DisplayAllEmployee),
    re_path(r'^api/employeesubmit', views.EmployeeSubmit),
    re_path(r'^api/employeelist', views.Employee_List),
    re_path(r'^api/employeebyid',views.Employee_List_By_Id),   
    re_path(r'^api/employeeupdatedelete',views.Employee_Update_Delete), 
    re_path(r'^api/display_employee_picture',views.Employee_Display_Picture),   
    re_path(r'^api/update_employee_image',views.UpdateEmployeeImage),
    
    
    
    re_path(r'^api/customerinterface',customerview.CustomerInterface),
    re_path(r'^api/customersubmit',customerview.CustomerSubmit),
    re_path(r'^api/displayallcustomer',customerview.DisplayAllCustomer),
    re_path(r'^api/customerlist',customerview.Customer_List),
    re_path(r'^api/customerbyid',customerview.Customer_List_By_Id),
    re_path(r'^api/customerupdatedelete',customerview.Customer_Update_Delete), 
    
    
    re_path(r'^api/login',login.Login),
    re_path(r'^api/admindashboard',login.AdminDashboard),
    re_path(r'^api/managerdashboard',login.ManagerDashboard),
    re_path(r'^api/employeedashboard',login.EmployeeDashboard),
    re_path(r'^api/checkadminlogin',login.Check_Admin_Login),
    re_path(r'^api/checkemployeelogin',login.Check_Employee_Login),
    re_path(r'^api/checkmanagerlogin',login.Check_Manager_Login),
    re_path(r'^api/logoutadmin',login.LogoutAdmin),
    
  
    
    re_path(r'^api/callcustomerbyid',callview.Customer_List_By_Id),
    re_path(r'^api/calldetailsubmit',callview.CallDetailSubmit),
    re_path(r'^api/displayfilldetail',callview.FillDetail),
    re_path(r'^api/displayfilllist',callview.Caller_List),
    re_path(r'^api/calllistbyid',callview.Caller_List_By_Id),
    re_path(r'^api/calldetailupdatedelete',callview.Caller_Update_Delete),
    
    
    
    re_path(r'^api/statelist', views.State_List),
    re_path(r'^api/citylist', views.City_List),
    
    re_path(r'^api/managerinterface', managerview.ManagerInterface),
    re_path(r'^api/managersubmit', managerview.ManagerSubmit),
    re_path(r'^api/displayallmanager', managerview.DisplayAllManager),
    re_path(r'^api/managerlist', managerview.Manager_List),
    re_path(r'^api/managerbyid', managerview.Manager_List_By_ID),
    re_path(r'^api/managerupdatedelete', managerview.Manager_Update_Delete),
    
    
   
]

from django.urls import path
from admin import views
from admin.views import *

urlpatterns = [
    path('',views.Counts,name='admindash'),
    path('login', views.Login.as_view(), name='login'),
    path('hospital', views.Hospital_details, name='hospital_details'),
    path('hospital_approval/<int:id>',  views.Hospital_approval, name='hospital_approval'),
    path('hospital_delete/<int:id>', views.Hospital_delete, name='hospital_delete'),
    path('department', views.Department_details, name='department_details'),
    path('department_add', views.Department_add.as_view(), name='department_add'),
    path('department_delete/<int:id>', views.Department_delete, name='department_delete'),
    path('user', views.User_details, name="user_details"),
    path('block_user/<int:id>', views.Block_user, name='block_user')

]

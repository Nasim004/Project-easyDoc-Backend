
from django.urls import path
from hospitalAccounts import views
from hospitalAccounts.views import *

urlpatterns = [

    path('<int:id>',views.Counts,name='hospitaldash'),
    path('signup',views.Sign_up.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('doctor_add',views.Doctor_add.as_view(),name='doctor_add'),
    path('doctor/<int:hospital_id>',views.Doctor_details,name="doctor"),
    path('doctor_available/<int:id>',views.Doctor_availablity,name="doctor availablity"),


]

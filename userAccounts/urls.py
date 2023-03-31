from django.urls import path
from userAccounts import views

urlpatterns = [

    path('signup',views.Sign_up.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('verifyToken',views.verifyToken,name='verifyToken'),
    path('myprofile/<int:id>',views.myProfile,name="myprofile"),
    path('profileupdate/<int:id>',views.profileUpdate,name='profileUpdate'),
    path('changepassword/<int:id>',views.change_password,name='changepassword'),
    path('randomhospital',views.randomHospital,name='randomHospital'),
    path('userhospital',views.Hospital_details,name='userhospital'),
]
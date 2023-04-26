from django.urls import path
from userAccounts import views

urlpatterns = [

    path('signup', views.Sign_up.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('verifyToken', views.verifyToken, name='verifyToken'),
    path('myprofile/<int:id>', views.myProfile, name="myprofile"),
    path('profileupdate/<int:id>', views.profileUpdate, name='profileUpdate'),
    path('changepassword/<int:id>', views.change_password, name='changepassword'),
    path('randomhospital', views.randomHospital, name='randomHospital'),
    path('userhospital', views.Hospital_details, name='userhospital'),
    path('hospital_detail/<int:id>', views.Hospital_detail, name='hospital_detail'),
    path('doctor_detail/<int:id>', views.Doctor_detail, name="doctor_detail"),
    path('booking', views.Bookings.as_view(), name='booking'),
    path('token/<int:id>', views.tokens, name='tokens'),
    path('optickets/<int:id>', views.optickets, name='optickets'),


]

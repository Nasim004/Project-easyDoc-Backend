
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('userAccounts.urls')),
    path('hospital/',include('hospitalAccounts.urls')),
    path('admin/',include('admin.urls')),
]



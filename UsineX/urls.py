from django.contrib import admin
from django.urls import path, include
from users.views import root_redirect

urlpatterns = [
    path('', root_redirect, name='root'),
    path('admin/', admin.site.urls),
    path('machines/', include('Machines.urls')), 
    path('users/', include('users.urls')), 
    
]

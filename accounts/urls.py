

from django.urls import path

from .views import *



urlpatterns = [
    path('',profile,name='profile_url'),
    path('logout',user_logout,name='logout_url'),
 
]
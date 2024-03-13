
from django.urls import path,re_path

from .views import *




urlpatterns = [
    path('',blog,name='blog_url'),
    path('<slug:slug>/',post,name='post_detail'),
    
]

from django.urls import path,re_path

from .views import *




urlpatterns = [
    path('',blog,name='blog_url'),
    path('<slug:pslug>/',post_detail,name='post_detail'),
    
]
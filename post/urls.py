
from django.urls import path,re_path

from .views import *




urlpatterns = [
    path('',blog,name='blog_url'),
    path('<slug:slug>/',post,name='post_detail'),
     path('tag/<slug:tag_slug>/',blog_view,name='posts_tag_url')
    
]
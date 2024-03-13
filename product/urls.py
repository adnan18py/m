from django.urls import path,include
from .views import *



urlpatterns = [
    path('',products_view,name='products_url'),
        path('<slug:slug>/',products_page_view),
        
        path('tag=<slug:tag_slug>/',products_view,name='pro_tag_url')
]


"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from home.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls,name='admin_url'),
    path('',home,name='home_url'),
    path('login/',user_login,name='login_url'),
    path('blog/', include('post.urls')),
    path("profile/",include('accounts.urls')),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'home.views.not_found'
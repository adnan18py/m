from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import *
from .forms import *
from django.contrib import messages



def home(request):
    
    return render(request,'home/home.html')






def not_found(request, exception):
     return render(request,'home/404.html')


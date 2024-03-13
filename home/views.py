from django.shortcuts import render
# from django.contrib.auth import
from .models import *
from .forms import *
from django.contrib import messages



def home(request):
    
    return render(request,'home/home.html')





def not_found(request, exception):
     return render(request,'home/404.html')


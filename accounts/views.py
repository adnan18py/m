from .forms import *
from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User


def profile(request):
     # if request.user.username != 'adnan':
     #      return redirect('home_url')
     if request.user.is_authenticated:
          return render(request,'accounts/profile_page.html')
     
     else:
          return redirect('login_url')




def user_login(request):
     if request.user.is_authenticated:
          return redirect('profile_url')
     else:
          if request.method == "POST":
               form=LoginForm(request.POST)
               if form.is_valid():
                    cd=form.cleaned_data
                    r=authenticate(request,username=cd['username'],password=cd['password'])
                    if cd['username'] == '':
                         messages.error(request,'نام کاربری نباید خالی باشد','warning')
                    if cd['password'] == '':
                         messages.error(request,'رمز عبور نباید خالی باشد','warning')
                    
                    
                    if r is not None:
                         login(request,r)
                         v=f'''
با موفقیت وارد حساب کاربری شدید
خوش آمدید{request.user.first_name}😊
'''
                         messages.success(request,v,'success')
                         return redirect('profile_url')
                    elif cd['password'] != '' :
                         if cd['username'] != '':
                              messages.error(request,'رمز عبور یا نام کاربری اشتباه است','warning')

          else:
               form=LoginForm()
          data={'form':form}
          

          return render(request,'accounts/login.html',data)



def user_logout(request):
     logout(request)
     messages.success(request,'با موفقیت از حساب کاربری خارج شدید' ,'success')
     return redirect('home_url')






def RegisterUser(request):
    if request.method == 'POST':
        form = RegisteritonForm(request.POST)
        if form.is_valid():
               cd = form.cleaned_data
               user=User.objects.create_user(cd['username'],cd['email'],cd['password'])
               user.first_name=cd['frist_name']
               user.last_name=cd['last_name']
               user.save()
               r=authenticate(request,username=cd['username'],password=cd['password'])
               login(request,r)
               return redirect('profile_url')
    else:
        form = RegisteritonForm()
    if request.user.is_authenticated:
         return redirect('profile_url')
    return render(request,'accounts/s.html',{'form':form})




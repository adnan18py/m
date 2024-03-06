from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def blog(request):
     # request.user
     posts = Post.objects.all()
     
     context={'posts':posts}
     
     return render(request,'post/blog.html',context=context)


def post(request, pk):
     user=request.user
     if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
               posts=Post.objects.get(pk=pk)
               cd = form.cleaned_data
               Comment.objects.create(text=cd['text'],post=posts,name=user)
               return redirect(f'/blog/{pk}')
               
     else:
          form = CommentForm()



     posts=Post.objects.get(pk=pk)
     comments=Comment.objects.filter(post=posts,)
     
     context={'post':posts,'comment':comments,'form':form}
     return render(request,'post/pos-page.html',context=context)





     
     


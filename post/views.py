from django.shortcuts import render, redirect,get_object_or_404
from post.models import *
from .forms import *
from django.contrib import messages





# def post_detail(request, pslug):
#     post = get_object_or_404(Post, slug=pslug)
#     related_posts = post.related_posts.all()
#     return render(request, 'post/pos-page.html', {'post': post, )
def blog(request):
     # request.user
     posts = Post.objects.all()
     
     context={'posts':posts}
     
     return render(request,'post/blog.html',context=context)


def post(request, slug):
     post = get_object_or_404(Post, slug=slug)
     related_posts = post.related_posts.all()
     user=request.user
     if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
               posts=Post.objects.get(slug=slug)
               cd = form.cleaned_data
               Comment.objects.create(text=cd['text2'],post=posts,name=user)
               return redirect(f'/blog/{slug}')
               
     else:
          form = CommentForm()



     posts=Post.objects.get(slug=slug)
     comments=Comment.objects.filter(post=posts,)
     
     context={'post':posts,'comment':comments,'form':form,'rel': related_posts}
     return render(request,'post/pos-page.html',context=context)





     
     


from django.shortcuts import render, redirect,get_object_or_404
from post.models import *
from .forms import *
from django.contrib import messages

from taggit.models import Tag




def blog(request):
     
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
               Comment.objects.create(text=cd['text'],post=posts,name=cd['name'])
               return redirect(f'/blog/{slug}')
        
     else:
          form = CommentForm()


     posts = Post.objects.filter(slug=slug)[:1]
     comments = Comment.objects.filter(post__in=posts)
     r = Reply.objects.filter(comment__in=comments)
  
     
     
     posts1=Post.objects.get(slug=slug)

     context={'post':posts1,'comment':comments,'form':form,'rel': related_posts,'l':r}
     return render(request,'post/pos-page.html',context=context)




def blog_view(request,tag_slug=None):
    posts=Post.objects.all()

    if tag_slug:
        tag=Tag.objects.get(slug=tag_slug)
        posts=posts.filter(tags__in=[tag])


    context={'posts':posts,'tag':tag}
    return render(request,"post/blog.html",context)

     
     


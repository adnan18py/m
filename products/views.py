from django.shortcuts import render,get_object_or_404
from .models import *
from post.models import Post


from taggit.models import Tag




def products_page_view(request,slug):
    product=Products.objects.get(slug=slug)
    images=Image.objects.filter(model=product)
    post = get_object_or_404(Products, slug=slug)
    related_posts = post.related_products.all()
    context={'product':product,
                 'images':images,
                 'rel':related_posts,
                
                 
                 }
    return render(request,'products\product.html',context)




def products_view(request,tag_slug=None):
    products=Products.objects.all()

    if tag_slug:
        tag=Tag.objects.get(slug=tag_slug)
        products=products.filter(tags__in=[tag])


    context={'products':products}
    return render(request,'products\products.html',context)












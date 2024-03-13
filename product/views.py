from django.shortcuts import render,get_object_or_404
from .models import *
from post.models import Post


from taggit.models import Tag




def products_page_view(request,slug):
    product=Product.objects.get(slug=slug)
    images=Image.objects.filter(model=product)
    products = get_object_or_404(Product, slug=slug)
    
    related_products = products.related_products.all()
    related_posts= products.related_posts.all()
    context={'product':product,
                 'images':images,
                 'rel':related_products,
                 'rel_post':related_posts
                
                 
                 }
    return render(request,'products\product.html',context)




def products_view(request,tag_slug=None):
    products=Product.objects.all()

    if tag_slug:
        tag=Tag.objects.get(slug=tag_slug)
        products=products.filter(tags__in=[tag])


    context={'products':products}
    return render(request,'products\products.html',context)












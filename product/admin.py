from django.contrib import admin
from .models import *


class CommentAdminInline(admin.TabularInline):
    model=Comment
    fields=['text','name']
    extra=0



class ImageAdminInline(admin.TabularInline):
    model=Image
    fields=['id','image']
    extra=0



class ProductsAdmin(admin.ModelAdmin):
    list_display=['title','price']
    
    inlines=[
        CommentAdminInline,
        ImageAdminInline
        ]











admin.site.register(Product,ProductsAdmin)

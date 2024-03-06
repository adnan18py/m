from django.contrib import admin
from .models import *


class CommentAdminInline(admin.TabularInline):
    model=Comment
    fields=['text','name']
    extra=0



class ImageAdminInline(admin.TabularInline):
    model=Image
    
    extra=0



class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','crated_time']
    inlines=[CommentAdminInline,ImageAdminInline]






admin.site.register(Post,PostAdmin)

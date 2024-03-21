from django.contrib import admin
from .models import *



class ReplyAdminInline(admin.TabularInline):
    model=Reply
    fields=['text','name']
    extra=0



    
class CommentAdmin(admin.ModelAdmin):
    list_display=['post','text','name']
    inlines=[
        ReplyAdminInline
    ]



class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','crated_time']
    prepopulated_fields = {"slug": ("title", "writer")}






admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
from django.contrib import admin
from .models import *


class CommentAdminInline(admin.TabularInline):
    model=Comment
    fields=['text','name']
    extra=0




class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','crated_time']
    prepopulated_fields = {"slug": ("title", "writer")}
    inlines=[CommentAdminInline]






admin.site.register(Post,PostAdmin)

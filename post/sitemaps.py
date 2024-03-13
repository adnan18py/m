from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post

class MyModelSitemap(Sitemap):
    def items(self):
        return Post.objects.all()


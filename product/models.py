from django.db import models
from taggit.managers import TaggableManager
from django.utils.text import slugify
from post.models import *




class Product(models.Model):
    title = models.CharField(max_length=100,verbose_name='نام محصول')
    cap = models.TextField(null=True,verbose_name='کپشن')
    text = models.TextField(null=True,verbose_name='توضیحات')
    img=models.ImageField(null=True,verbose_name='عکس محصول')
    price=models.PositiveIntegerField(null=True,verbose_name='(تومان)قیمت محصول')
    alt=models.CharField(max_length=100,verbose_name='موضوع تصویر',null=True)
    
    related_products = models.ManyToManyField('self', blank=True)
    related_posts = models.ManyToManyField(Post)
    slug = models.SlugField(max_length=50, allow_unicode=True,verbose_name='آدرس  پست',unique=True,null=True)
    tags=TaggableManager()
    off=models.BooleanField(default=False)
    off_price=models.CharField(max_length=2,null=True,)






    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)

class Comment(models.Model):
    name=models.CharField(max_length=100,null=True,verbose_name='نام کاربری')
    model=models.ForeignKey(Product, on_delete=models.CASCADE)
    text=models.TextField(verbose_name='متن کامنت')


class Image(models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')



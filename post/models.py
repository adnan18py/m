from django.db import models
from taggit.managers import TaggableManager



class Post(models.Model):
    
    title = models.CharField(max_length=100,verbose_name='عنوان')
    text = models.TextField(null=True,verbose_name='متن')
    writer = models.CharField(max_length=30,verbose_name='نویسنده')
    img = models.ImageField(null=True,upload_to='images',verbose_name='عکس')
    crated_time = models.DateTimeField(null=True,auto_now_add=True)
    tags=TaggableManager()
    
    
    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)


class Comment(models.Model):
    name=models.CharField(max_length=100,null=True,verbose_name='نام کاربری')
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField(verbose_name='متن کامنت')


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField(blank=True)
    write=models.CharField(max_length=30)
    def __str__(self):
        return '{}-{}'.format(self.pk,self.title)


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.TextField()

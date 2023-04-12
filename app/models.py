from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    profile = models.ImageField(upload_to='profile/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    blog = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    post_img = models.ImageField(upload_to='postimg/')

    def __str__(self) -> str:
        return self.title
    

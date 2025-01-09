from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title= models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category=models.ManyToManyField(Category)

    content=models.TextField()
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateField(null=True, blank=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
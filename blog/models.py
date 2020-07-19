from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
# author
# title
# text
# create
# publish
from django.utils import timezone


# class User():
#     pass



class Post(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title


from django.utils import timezone
from django.db import models
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_published = models.DateField(blank=True,null=True)

class Comments(models.Model):
    post = models.ForeignKey('Post',related_name='comments')
    author = models.CharField(max_length=264)
    text = models.TextField()
    data_published = models.DateField()

from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now ,blank=True)
    date_updated = models.DateTimeField( auto_now=True)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

class Comment(models.Model):
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    question = models.ForeignKey(Post,on_delete=models.CASCADE)

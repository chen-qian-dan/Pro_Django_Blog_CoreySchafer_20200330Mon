from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # attribute is field in database
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete=models.CASCADE means if the user is deleted, 
    # we want to delete all the posts from that user as well. 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
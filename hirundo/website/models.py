from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.TextField(blank=True)
    author = models.ForeignKey(User)


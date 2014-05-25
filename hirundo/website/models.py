from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.TextField(blank=True)

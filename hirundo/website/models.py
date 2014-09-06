from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(blank=False)
    pub_date = models.DateTimeField(auto_now=True)
    location = models.TextField(blank=True)
    author = models.ForeignKey(User)


class UserFollowingRelationship(models.Model):
    follower = models.ForeignKey(User, related_name="user_follower")
    followed = models.ForeignKey(User, related_name="user_followed")

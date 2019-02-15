# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User
from posts.models import Post

# Create your models here.
#user
class Comment(models.Model):
    content = models.TextField
    user = models.ForeignKey(User,related_name='user_comments')
    post = models.ForeignKey(Post, related_name='post_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Follow(models.Model):
    from_user = models.ForeignKey(User,related_name='followers')
    to_user = models.ForeignKey(User,related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Favorite(models.Model):
    user = models.ForeignKey(User,related_name='userlikes')
    post = models.ForeignKey(Post,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
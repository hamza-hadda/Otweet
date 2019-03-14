# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import User


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Post(models.Model):
    content = models.TextField(null=True)
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)

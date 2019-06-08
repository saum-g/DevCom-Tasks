# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length = 140)
    username=models.CharField(max_length=140)
    body = models.TextField()
    date =models.DateTimeField()

    def __str__(self):
        return self.title


# Create your models here.

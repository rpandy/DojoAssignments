# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#Create your models here.
class SecretsManager(models.Manager):
    pass


class Secret(models.Model):
    secret = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey('auth.User') #if you have a user class in another app will the foreign key link to said class?

    objects = SecretsManager()

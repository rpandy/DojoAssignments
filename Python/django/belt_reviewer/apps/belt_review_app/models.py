# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from ..login_and_registration_app.models import User
#
# # Create your models here.
# class Review(models.Model):
#     review = models.TextField()
#     rating = models.IntegerField(default=0)
#     user_id = models.ForeignKey(User, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     objects = ReviewManager()
#
# class Book(models.Model):
#     title = models.CharField(max_length = 300)
#     review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     objects = BookManager()
#
# class Author(models.Model):
#     name = models.CharField(max_length = 150)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     objects = AuthorManager()

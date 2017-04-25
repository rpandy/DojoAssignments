# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_and_registration_app.models import User


# Create your models here.
class ReviewManager(models.Manager):
    def create_review(self,data):
        print "creating new review"
        print "*************"
        print data, "<<--here is the data from the validations and/or database"
        # print "$$$$$$$$$$$$", data['user_id']

        # print "user_id!!!!!!!!!!:", User.objects.get(user_id=data['user_id'])
        errors = []
        #validate length of review (>1 char/ < 300)
        if len(data['review']) < 1:
            print "Review cannot be empty"
            errors.append("Review cannot be empty")
        if len(data['title']) < 1:
            print "Title cannot be empty"
            errors.append("Review cannot be empty")
        if len(data['review']) > 300:
            print "Review cannot be longer than 300 characters"
            errors.append("Review cannot be longer than 300 characters")
        if len(data['author']) < 1:
            print "Author cannot be empty"
            errors.append("Review cannot be empty")
        if len(data['author']) > 150:
            print "Author's name cannot exceed 150 characters"
            errors.append("Author's name cannot exceed 150 characters")
        if errors:
            return(False,errors)
        else:
            print "Adding data to database"
            # user_id = User.objects.get(id=data['user_id']) #get id from Login and reg models.py
            # user = User.objects.get(user_id=data['user_id']) #get id from Login and reg models.py

            new_review = Review.objects.create(
                review = data['review'],
                rating = data['rating'],
                # user = user,
            )
    # def get_rating(request):
    #     new_rating = Review.objects.get(rating=data['rating'])

            print "data was added!"
            return(True,new_review)

class BookManager(models.Manager):
    pass
class AuthorManager(models.Manager):
    pass

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, null=True)
    #book_id = models.ForeignKey(Book,on_delete=models.CASCADE)<------ADD
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()

class Book(models.Model):
    title = models.CharField(max_length = 300)
    #review_id = models.ForeignKey(Review, on_delete=models.CASCADE) <---- REMOVE 
    #author_id = models.ForeignKey(Author,on_delete=models.CASCADE) <------ADD 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()

class Author(models.Model):
    name = models.CharField(max_length = 150)
    #book_id = models.ForeignKey(Book,on_delete=models.CASCADE) <------ADD 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def validate_and_create(self,data):
        print data, "WOW WE HAVE DATA"
        errors = []

        if len(data['email']) < 1:
            print "EMAIL CANNOT BE BLANK"
            # flash("EMAIL CANNOT BE BLANK")
            errors.append("EMAIL CANNOT BE BLANK")
        if not EMAIL_REGEX.match(data['email']):
            print "EMAIL IS NOT VALID"
            # flash("EMAIL IS NOT VALID")
            errors.append("EMAIL IS NOT VALID")
        if errors:
            return (False, errors)
        else:
            #we add to database
            new_object = User.objects.create(
                email=data['email']
            )
            return (True, new_object)
    #if validation passes then insert email into database:

class User(models.Model):
    email = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # connect an instance of UserManager to our User model
    # which essentially overwrites the old hidden object's
    # key with a new on containing extra properties.

    objects = UserManager()













# print "login logic here!"
# print "If successful login occurs pass back a tuble with (True, user)"
# print "If not successful pass back a tuble with (False, 'Login unsuccessful')"
# return ("This will contain validations")

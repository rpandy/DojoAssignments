# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import F
from ..login_and_registration_app.models import User

#Create your models here.
class SecretManager(models.Manager):
    #handling secrets
    #The self parameter includes all the information about the individual object that has called the method.
    def current_user(self, id):
        print "This is the current_user method"
        print "*************"

        current_user_id = User.objects.get(id=id) # <--- using session in views. passing id as parameter TRY id = data=['user_id']

        print "current user id",current_user_id

        return current_user_id #returning current user id ONLY

    def create_new_secret(self,data):
        print "creating new secret"
        print "*************"
        print data, "<<--here is the data from the validations and/or database"


        errors = []
        #validate length of secret (>1 char/ < 300)
        if len(data['secret']) < 1:
            print "Secret cannot be empty"
            errors.append("Secret cannot be empty")
        if len(data['secret']) > 300:
            print "Secret cannot be longer than 300 characters"
            errors.append("Secret cannot be longer than 300 characters")
        if errors:
            return(False,errors)
        else:
            print "Lets add data to database"
            # session_user = Secret.objects.current_user(data)
            # print "this is the User variable:", current_user(data)
            # user_id = request.session.user_id
            new_secret = Secret.objects.create(
                secret = data['secret'],
                # user_id = user_id
            )
            print "secret should be added here!"

            return(True,new_secret) # <--- send tuple to views

    def recent_secret_5(request):
        top_5_secrets = Secret.objects.order_by('-created_at')[:5]
        return top_5_secrets

    def popular_secrets(request):
        # popular_secrets = Secret.objects.order_by('created_at')[:10]
        popular_secrets = Secret.objects.order_by('likes')[:10]
        return popular_secrets

    def like_secret(id):
        print "Like secret"
        print "*************"
        #CHECK OUT THE DOCUMENTATION
        like = Secret.objects.get(id=id)
        like.update(likes=F('likes')+1)
        return (True,)

    def delete(request,data):
        # print "CURRENT USER METHOD:", current_user(request)
        pass

# class Like(models.Model):
#     likes = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Secret(models.Model):
    secret = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, null=True) #if you have a user class in another app will the foreign key link to said class?

    objects = SecretManager()

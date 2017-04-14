# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Course

def index(request):
    print "This is the index route!"
    print "********"

    context = {
        'courses': Course.objects.all()
        #select * from courses
    }

    return render(request,"courses_app/index.html", context)

def courses(request):
    print "This is the (add) courses route"
    print "************"

    if request.method == 'POST':
        #insert course name, description, created_at & updated at into database.
        Course.objects.create(course_name=request.POST['name'], course_description=request.POST['description'])

        courses = Course.objects.all()

        print "Courses:",(courses)
    else:
        redirect('/')

    return redirect('/')

def verify(request, id):
    print "Verifying the course we want to delete!"

    #get specific course to delete
    specific_course = Course.objects.get(id=id)
    context = {
        'specific_course': specific_course
        #select * from courses
    }
    print "specific course:", specific_course.id
    return render(request,"courses_app/courses.html", context)


def destroy(request, id):
    print "This is the destroy route!"
    course_to_delete = Course.objects.get(id=id)
    print "This is the course we deleted:", course_to_delete.id, "-", course_to_delete.course_name

    course_to_delete.delete()
    return redirect('/')

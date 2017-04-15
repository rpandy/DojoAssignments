from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/(?P<color>\D{3,6})/$', views.one_ninja) #pattern - between 3 and 6 letters passed from 'color'
]

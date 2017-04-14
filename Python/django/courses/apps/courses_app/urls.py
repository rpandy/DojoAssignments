from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.courses),
    url(r'^courses/verify/(?P<id>\d+)$', views.verify),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
]

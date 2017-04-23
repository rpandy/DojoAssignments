from django.conf.urls import url
from . import views

app_name = 'secret'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^logout$', views.logout, name='logout'),
]

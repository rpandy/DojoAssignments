from django.conf.urls import url
from . import views

app_name = 'review'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^new_review/$', views.new_review, name='new_review'),
    # url(r'^new_review/(?P<id>\d+)$', views.new_review, name='new_review'),
    # url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]

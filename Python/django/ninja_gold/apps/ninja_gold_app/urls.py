from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money/farm$', views.process_farm),
    url(r'^process_money/cave$', views.process_cave),
    url(r'^process_money/house$', views.process_house),
    url(r'^process_money/casino$', views.process_casino),
    url(r'^clear$', views.clear),    
]

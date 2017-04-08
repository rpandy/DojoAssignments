from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate_number$', views.generate),
    url(r'^clear$', views.clear)
]

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.survey_process),
    url(r'^results$', views.results),
    url(r'^home$', views.home),
    url(r'^clear$', views.clear),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<subject_name>[\w|\W]+)/qty$', views.practicals, name='practicals'),
    url(r'^(?P<subject_name>[\w|\W]+)/(?P<practical_id>[0-9]+)/$', views.details, name='details'),
]
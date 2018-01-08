from django.conf.urls import url
from django.contrib import admin
from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^create/$', post_create, name='create_post'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update_post'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete_post'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^landing', views.landing),
    url(r'^go_process', views.go_process),
]
from django.urls import path, include
from . import views

# hello 안에 hello 와 hello01이 존재
#
urlpatterns = [
    path("", views.index),
    path("text/", views.test),


]
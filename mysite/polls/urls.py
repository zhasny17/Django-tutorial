from django.urls import path, re_path

from . import views

urlpatterns = [
    path('test', views.index, name='index'),
]
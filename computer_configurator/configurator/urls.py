from django.contrib import admin
from django.urls import path
from . import views
from .views import configure_computer

urlpatterns = [
     path('', configure_computer, name='configure_computer'),
]
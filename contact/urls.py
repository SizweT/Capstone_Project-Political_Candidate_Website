# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_feedback, name='contact'),
]

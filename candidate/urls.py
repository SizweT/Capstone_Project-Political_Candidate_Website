# candidate/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.candidate_profile_view, name='candidate_profile'),
    path('profile/create/', views.create_candidate_profile, name='create_candidate_profile'),
    # Add URLs for user authentication (login, logout, signup)
]

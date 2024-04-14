# Project:  political_candidate_website/urls.py
from django.contrib import admin
from django.urls import path, include
from candidate.views import profile, login_view, logout_view
from user_auth import views as auth_views
from django.views.generic import TemplateView
from contact.views import send_feedback

urlpatterns = [
    path('admin/', admin.site.urls),

    # Handles the root path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('welcome/', TemplateView.as_view(template_name='welcome.html'), name='welcome'),

    # candidate URL
    path('profile/', profile, name='candidate_profile'),
    path('login/', login_view, name='candidate-login'),
    path('logout/', logout_view, name='candidate-logout'),


    # Include Django's authentication URLs after your candidate URLs
    path('', include('django.contrib.auth.urls')),

    # Add URL for user registration,login and logout
    path('register/', auth_views.register, name='register'),

    # Add URL for contact form
    path('contact/', send_feedback, name='contact'),
]


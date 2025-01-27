# candidate/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CandidateProfileForm
from .models import Candidate
from django.contrib.auth import authenticate, login, logout


@login_required
def profile(request):
    # Retrieve candidate object from the database
    candidate = Candidate.objects.first()  # Assuming there's only one candidate for simplicity

    # Pass candidate object to the template context
    context = {'candidate': candidate}
    return render(request, 'profile.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')

# contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def send_feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

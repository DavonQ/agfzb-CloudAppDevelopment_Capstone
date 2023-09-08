from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')

# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'djangoapp/login.html')

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return redirect('login')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == "POST":
        # Handle user registration logic here
        # ...
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')
    return render(request, 'djangoapp/registration.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    # Add logic to retrieve dealer details and reviews by dealer_id
    # ...
    context = {}  # Replace with actual context data
    return render(request, 'djangoapp/dealer_details.html', context)

# Create an `add_review` view to submit a review
def add_review(request, dealer_id):
    if request.method == "POST":
        # Handle review submission logic here
        # ...
        messages.success(request, 'Review submitted successfully.')
    return redirect('get_dealer_details', dealer_id=dealer_id)

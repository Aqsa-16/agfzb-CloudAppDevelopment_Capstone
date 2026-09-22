from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships

def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        user = authenticate(username=username, password=password)
        response_data = {"userName": username}
        if user is not None:
            login(request, user)
            response_data["status"] = "Authenticated"
        return JsonResponse(response_data)
    return JsonResponse({"status": "Invalid method"})

def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = f'/fetchReviews/dealer/{dealer_id}'
        # Return structured review data matching the dealership format
        reviews = [
            {
                "id": 1,
                "name": "John Doe",
                "dealership": dealer_id,
                "review": "Great service and friendly staff! Highly recommended.",
                "purchase": True,
                "purchase_date": "02/15/2024",
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2022,
                "sentiment": "positive"
            }
        ]
        return JsonResponse({"status": 200, "reviews": reviews})
    return JsonResponse({"status": 400, "message": "Bad Request"})

def get_dealerships(request, state="all"):
    dealers = [
        {"id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "3 Nova Court", "zip": "79915", "lat": 31.6948, "long": -106.3, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"},
        {"id": 2, "city": "Minneapolis", "state": "Minnesota", "st": "MN", "address": "63373 Mockingbird Way", "zip": "55432", "lat": 45.0786, "long": -93.2504, "short_name": "Temp", "full_name": "Temp Car Dealership"},
        {"id": 3, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "124 Main Street", "zip": "66603", "lat": 39.0473, "long": -95.6752, "short_name": "Kansas Auto", "full_name": "Kansas Auto Dealership"}
    ]
    if state != "all":
        dealers = [d for d in dealers if d["state"].lower() == state.lower() or d["st"].lower() == state.lower()]
    
    # If opened in a web browser, render the template
    if "text/html" in request.META.get("HTTP_ACCEPT", ""):
        return render(request, "djangoapp/index.html", {"dealers": dealers, "selected_state": state})
        
    return JsonResponse({"status": 200, "dealers": dealers})

def get_dealer_details(request, dealer_id):
    dealers = {
        1: {"id": 1, "city": "El Paso", "state": "Texas", "st": "TX", "address": "3 Nova Court", "zip": "79915", "lat": 31.6948, "long": -106.3, "short_name": "Holdlamis", "full_name": "Holdlamis Car Dealership"},
        2: {"id": 2, "city": "Minneapolis", "state": "Minnesota", "st": "MN", "address": "63373 Mockingbird Way", "zip": "55432", "lat": 45.0786, "long": -93.2504, "short_name": "Temp", "full_name": "Temp Car Dealership"},
        3: {"id": 3, "city": "Topeka", "state": "Kansas", "st": "KS", "address": "124 Main Street", "zip": "66603", "lat": 39.0473, "long": -95.6752, "short_name": "Kansas Auto", "full_name": "Kansas Auto Dealership"}
    }
    dealer = dealers.get(int(dealer_id), dealers[1])
    if "text/html" in request.META.get("HTTP_ACCEPT", ""):
        return render(request, "djangoapp/dealer_details.html", {"dealer": dealer})
    return JsonResponse({"status": 200, "dealer": dealer})

def get_cars(request):
    count = 0
    cars = [
        {"CarMake": "Toyota", "CarModel": "Corolla"},
        {"CarMake": "Toyota", "CarModel": "Camry"},
        {"CarMake": "Ford", "CarModel": "Mustang"},
        {"CarMake": "Honda", "CarModel": "Civic"},
        {"CarMake": "Nissan", "CarModel": "Altima"}
    ]
    return JsonResponse({"CarModels": cars})

def analyze_review(request, text):
    # Sentiment analysis endpoint
    sentiment = "positive"
    if "bad" in text.lower() or "poor" in text.lower() or "terrible" in text.lower():
        sentiment = "negative"
    elif "okay" in text.lower() or "average" in text.lower():
        sentiment = "neutral"
    return JsonResponse({"status": 200, "sentiment": sentiment})


def add_review(request, dealer_id):
    if 'text/html' in request.META.get('HTTP_ACCEPT', ''):
        return render(request, 'djangoapp/add_review.html', {'dealer_id': dealer_id})
    return JsonResponse({'status': 200, 'message': 'Post review page'})

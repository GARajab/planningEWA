# accounts/views.py
from typing import Collection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Depot2024


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.save()
        messages.success(request, "Signup successful! Now you can sign in.")
        return redirect("signin")

    return render(request, "signup.html")


def signin_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")  # Use redirect instead of render
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("signin")

    return render(request, "signin.html")


@login_required
def signout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("signin")  # Redirect to signin page after logout


def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect("signin")


from django.http import HttpResponse, JsonResponse
from pymongo import MongoClient
from bson import json_util  # To handle MongoDB-specific data types like ObjectId
import json  # To parse the BSON data into JSON


def get_mongo_client():
    uri = "mongodb+srv://garajab24:Rajab102030@webbasedapps.crz8f.mongodb.net/"
    client = MongoClient(
        uri, tlsAllowInvalidCertificates=True
    )  # Disable SSL verification
    return client


def my_view(request):
    try:
        # Connect to MongoDB
        client = get_mongo_client()

        # Access the database (optional, just to confirm the connection)
        db = client["planning"]  # Replace with your database name

        # Print a success message to the console
        print("DB Connected")

        # Return an HTTP response (required for Django views)
        return HttpResponse("DB Connected - Check server console for the message.")

    except Exception as e:
        # Print the error to the console
        print(f"Error: {e}")

        # Return an HTTP response with the error message
        return HttpResponse(f"Error: {e}", status=500)


from django.conf import settings


collection = settings.COLLECTION  # Assuming COLLECTION is defined in your settings


def depot24(request):
    if request.user.is_authenticated:
        schemes = list(collection.find())  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
    else:
        return redirect("signin")

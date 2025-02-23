# accounts/views.py
from typing import Collection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .db import (
    COLLECTION_DEPOT2024,
    COLLECTION_DEPOT2025,
    COLLECTION_LR2024,
    COLLECTION_LR2025,
    COLLECTION_NC2024,
)


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


def depot24(request):
    if request.user.is_authenticated:
        schemes = list(
            COLLECTION_DEPOT2024.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
    else:
        return redirect("signin")


def depot25(request):
    if request.user.is_authenticated:
        schemes = list(
            COLLECTION_DEPOT2025.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot25.html", context)
    else:
        return redirect("signin")


def lr24(request):
    if request.user.is_authenticated:
        schemes = list(
            COLLECTION_LR2024.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
    else:
        return redirect("signin")


def lr25(request):
    if request.user.is_authenticated:
        schemes = list(
            COLLECTION_LR2025.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
    else:
        return redirect("signin")


def nc24(request):
    if request.user.is_authenticated:
        schemes = list(
            COLLECTION_NC2024.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "nc2024.html", context)
    else:
        return redirect("signin")

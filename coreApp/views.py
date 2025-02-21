# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


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
            return redirect("home")  # Redirect to your desired page after login
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("signin")

    return render(request, "signin.html")


def signout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("signin")  # Redirect to signin page after logout

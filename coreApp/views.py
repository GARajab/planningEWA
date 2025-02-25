# accounts/views.py
from typing import Collection
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import depotcases2024, depotcases2025, Permit

from django.views.decorators.http import require_POST


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
            messages.success(
                request, "Welcome " + username + " You Logged in successfully!"
            )
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


def depot24(request):
    if request.user.is_authenticated:
        schemes = depotcases2024.objects.all()

        return render(
            request,
            "depot24.html",
            {
                "schemes": schemes,
                "is_admin": request.user.is_superuser,
            },
        )
    else:
        return redirect("signin")


def depot25(request):
    if request.user.is_authenticated:
        schemes = depotcases2025.objects.all()
        # Fetch all documents from the collection
        context = {"schemes": schemes, "is_admin": request.user.is_superuser}
        return render(request, "depot25.html", context)
    else:
        return redirect("signin")


def lr24(request):
    if request.user.is_authenticated:
        # schemes = Depot2024.objects.all()  # Fetch all documents from the collection
        # context = {"schemes": schemes}
        # return render(request, "depot24.html", context)
        # else:
        return redirect("signin")


def lr25(request):
    if request.user.is_authenticated:
        schemes = list(
            # COLLECTION_LR2025.find()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
    else:
        return redirect("signin")


def nc24(request):
    if request.user.is_authenticated:
        permits = Permit.objects.all()
        return render(
            request,
            "nc2024.html",
            {"permits": permits, "is_admin": request.user.is_superuser},
        )
    else:
        return redirect("signin")


def get_permit(request, permit_id):
    permit = get_object_or_404(Permit, id=permit_id)
    data = {
        "id": permit.id,
        "Number": permit.Number,
        "REF_NO": permit.REF_NO,
        "TO_WL_DATE": permit.TO_WL_DATE,
        "Block": permit.Block,
        "KW": permit.KW,
        "KVA": permit.KVA,
        "TO_GIS_DATE ": permit.TO_GIS_DATE,
        "Plan_Status": permit.Plan_Status,
        "PASSED_DATE": permit.PASSED_DATE.strftime(
            "%Y-%m-%d"
        ),  # Format date for input field
    }
    return JsonResponse(data)


@csrf_exempt
def edit_permit(request):
    if request.method == "POST":
        permit_id = request.POST.get("permitId")
        permit = get_object_or_404(Permit, id=permit_id)

        # Update the permit object with form data
        permit.Number = request.POST.get("Number")
        permit.REF_NO = request.POST.get("REF_NO")
        permit.TO_WL_DATE = request.POST.get("TO_WL_DATE")
        permit.Block = request.POST.get("Block")
        permit.KW = request.POST.get("KW")
        permit.KVA = request.POST.get("KVA")
        permit.TO_GIS_DATE = request.POST.get("TO_GIS_DATE")
        permit.Plan_Status = request.POST.get("Plan_Status")
        permit.PASSED_DATE = request.POST.get("PASSED_DATE")
        permit.save()

        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})


def delete_depot24(request, permit_id):
    if request.method == "POST":
        depot_case = get_object_or_404(depotcases2024, id=permit_id)
        print(depot_case)
        depot_case.delete()
        messages.success(
            request, "Scheme " + depot_case.REFRENCENUMBER + " Deleted Successfully."
        )
        return redirect("depot24")
    else:
        messages.error(request, "Invalid request Record Not Deleted.")
    return redirect("depot24")


def delete_depot25(request, permit_id):
    if request.method == "POST":
        depot_case = get_object_or_404(depotcases2025, id=permit_id)
        depot_case.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect("depot25")
    else:
        messages.error(request, "Invalid request Record Not Deleted.")
    return redirect("depot25")


def update_depot_case(request, id):
    case = get_object_or_404(depotcases2024, id=id)

    # For GET request, send case data as JSON
    case_data = {
        "id": case.id,
        "REFRENCENUMBER": case.REFRENCENUMBER,
        "DEPOT": case.DEPOT,
        "AREA_ENGINEER_NAME": case.AREA_ENGINEER_NAME,
        "BLOCKNUMBER": case.BLOCKNUMBER,
        "SUBSTATIONNUMBER": case.SUBSTATIONNUMBER,
        "TX": case.TX,
        "FEEDERNUMBER": case.FEEDERNUMBER,
        "LVBNUMBER": case.LVBNUMBER,
        "TYPE": case.TYPE,
        "WAYLEAVENUMBER": case.WAYLEAVENUMBER,
        "USPDATE": case.USPDATE,
        "PASSEDDATE": case.PASSEDDATE,
        "REMARKES": case.REMARKES,
        "PlanStatus": case.PlanStatus,
        "ConStatus": case.ConStatus,
        "GISDATE": case.GISDATE,
        "RCCDATE": case.RCCDATE,
        "MSPDATE": case.MSPDATE,
        "labourcost": str(
            case.labourcost
        ),  # Convert Decimal to String for JSON serialization
        "ministrycost": str(
            case.ministrycost
        ),  # Convert Decimal to String for JSON serialization
        "cable_length": str(
            case.cable_length
        ),  # Convert Decimal to String for JSON serialization
        "Area": case.Area,
        "gov": case.gov,
        "sentDate": case.sentDate,
        "noOfServ": case.noOfServ,
        "noOfFaults": case.noOfFaults,
        "areaEngEmail": case.areaEngEmail,
        "EngPhoneNumber": case.EngPhoneNumber,
        "AreaOfAe": case.AreaOfAe,
        "totalcost": str(
            case.totalcost
        ),  # Convert Decimal to String for JSON serialization
    }

    if request.method == "POST":
        # Collect data from request.POST and update the instance
        for field in case._meta.get_fields():
            if field.name in request.POST:
                setattr(case, field.name, request.POST[field.name])
        case.save()
        messages.success(
            request, "Scheme " + case.REFRENCENUMBER + " is updated successfully!"
        )
        return JsonResponse({"success": True})
    return JsonResponse(case_data)


def update_depot_case25(request, id):
    case = get_object_or_404(depotcases2025, id=id)

    # For GET request, send case data as JSON
    case_data = {
        "id": case.id,
        "REFRENCENUMBER": case.REFRENCENUMBER,
        "DEPOT": case.DEPOT,
        "AREA_ENGINEER_NAME": case.AREA_ENGINEER_NAME,
        "BLOCKNUMBER": case.BLOCKNUMBER,
        "SUBSTATIONNUMBER": case.SUBSTATIONNUMBER,
        "TX": case.TX,
        "FEEDERNUMBER": case.FEEDERNUMBER,
        "LVBNUMBER": case.LVBNUMBER,
        "TYPE": case.TYPE,
        "WAYLEAVENUMBER": case.WAYLEAVENUMBER,
        "USPDATE": case.USPDATE,
        "PASSEDDATE": case.PASSEDDATE,
        "REMARKES": case.REMARKES,
        "PlanStatus": case.PlanStatus,
        "ConStatus": case.ConStatus,
        "GISDATE": case.GISDATE,
        "RCCDATE": case.RCCDATE,
        "MSPDATE": case.MSPDATE,
        "labourcost": str(
            case.labourcost
        ),  # Convert Decimal to String for JSON serialization
        "ministrycost": str(
            case.ministrycost
        ),  # Convert Decimal to String for JSON serialization
        "cable_length": str(
            case.cable_length
        ),  # Convert Decimal to String for JSON serialization
        "Area": case.Area,
        "gov": case.gov,
        "sentDate": case.sentDate,
        "noOfServ": case.noOfServ,
        "noOfFaults": case.noOfFaults,
        "areaEngEmail": case.areaEngEmail,
        "EngPhoneNumber": case.EngPhoneNumber,
        "AreaOfAe": case.AreaOfAe,
        "totalcost": str(
            case.totalcost
        ),  # Convert Decimal to String for JSON serialization
    }

    if request.method == "POST":
        # Collect data from request.POST and update the instance
        for field in case._meta.get_fields():
            if field.name in request.POST:
                setattr(case, field.name, request.POST[field.name])
        case.save()
        messages.success(
            request, "Scheme " + case.REFRENCENUMBER + " is updated successfully!"
        )
        return JsonResponse({"success": True})
    return JsonResponse(case_data)


def dep24Rep_view(request):
    return render(request, "dep24Rep.html")

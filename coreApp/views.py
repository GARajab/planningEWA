# accounts/views.py

from typing import Collection
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import depotcases2024, depotcases2025, Permit, LoadReading2024
from django.db.models import Sum
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


from django.http import JsonResponse


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

        return render(
            request,
            "depot25.html",
            {
                "schemes": schemes,
                "is_admin": request.user.is_superuser,
            },
        )
    else:
        return redirect("signin")


def lr24(request):
    if request.user.is_authenticated:
        schemes = (
            depotcases2024.objects.all()
        )  # Fetch all documents from the collection
        context = {"schemes": schemes}
        return render(request, "depot24.html", context)
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


@csrf_exempt
def edit_permit(request, permit_id):
    print(f"Received request with permit_id: {permit_id}")  # Debugging log
    if request.method == "GET":
        try:
            permit = Permit.objects.get(id=permit_id)
            print(f"Found permit: {permit}")  # Debugging log
            data = {
                "id": permit.id,
                "Number": permit.Number,
                "parcel_number": permit.parcel_number,
                "block": permit.block,
                "kw": permit.kw,
                "kva": permit.kva,
                "plan_status": permit.plan_status,
                "passed_date": (permit.passed_date),
                "to_wl_date": (permit.to_wl_date),
                "to_gis_date": (permit.to_gis_date),
                "wl_number": permit.wl_number,
                "ref_no": permit.ref_no,
                "comment": permit.comment,
            }
            return JsonResponse(data)
        except Permit.DoesNotExist:
            print(f"Permit with id {permit_id} does not exist.")  # Debugging log
            return JsonResponse(
                {"status": "error", "message": "Permit not found"}, status=404
            )
    elif request.method == "POST":
        try:
            permit = Permit.objects.get(id=permit_id)
            permit.Number = request.POST.get("Number")
            permit.parcel_number = request.POST.get("parcel_number")
            permit.block = request.POST.get("block")
            permit.kw = request.POST.get("kw")
            permit.kva = request.POST.get("kva")
            permit.plan_status = request.POST.get("plan_status")
            permit.passed_date = request.POST.get("passed_date")
            permit.to_wl_date = request.POST.get("to_wl_date")
            permit.to_gis_date = request.POST.get("to_gis_date")
            permit.wl_number = request.POST.get("wl_number")
            permit.ref_no = request.POST.get("ref_no")
            permit.comment = request.POST.get("comment")
            permit.save()
            return JsonResponse({"status": "success"})
        except Permit.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Permit not found"}, status=404
            )
    else:
        return JsonResponse(
            {"status": "error", "message": "Invalid request method"}, status=400
        )


def delete_Nc(request, permit_id):
    if request.method == "POST":
        permitNc = get_object_or_404(Permit, id=permit_id)
        permitNc.delete()
        messages.success(
            request, "Permit Number " + permitNc.Number + " Deleted Successfully."
        )
        return redirect("nc24")
    else:
        messages.error(request, "Invalid request Record Not Deleted.")
    return redirect("nc2024")


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


def update_depot24(request, id):
    case = get_object_or_404(depotcases2024, id=id)

    # For GET request, send case data as JSON
    case_data = {
        "id": case.id,
        "REFRENCENUMBER": case.REFRENCENUMBER,
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
        "labourcost": case.labourcost,  # Convert Decimal to String for JSON serialization
        "ministrycost": case.ministrycost,  # Convert Decimal to String for JSON serialization
        "cable_length": case.cable_length,  # Convert Decimal to String for JSON serialization
        "noOfServ": case.noOfServ,
        "noOfFaults": case.noOfFaults,
        "areaEngEmail": case.areaEngEmail,
        "totalcost": case.totalcost,  # Convert Decimal to String for JSON serialization
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


def update_depot25(request, id):
    case = get_object_or_404(depotcases2025, id=id)

    # For GET request, send case data as JSON
    case_data = {
        "id": case.id,
        "REFRENCENUMBER": case.REFRENCENUMBER,
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
        "labourcost": case.labourcost,  # Convert Decimal to String for JSON serialization
        "ministrycost": case.ministrycost,  # Convert Decimal to String for JSON serialization
        "cable_length": case.cable_length,  # Convert Decimal to String for JSON serialization
        "noOfServ": case.noOfServ,
        "noOfFaults": case.noOfFaults,
        "areaEngEmail": case.areaEngEmail,
        "totalcost": case.totalcost,  # Convert Decimal to String for JSON serialization
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


def depot24Report(request):
    if not request.user.is_authenticated:
        return redirect("signin")

    engineer_names = [
        "A RAJESH",
        "Bassam",
        "MOHAMED RAJAB",
        "MOHAMED ALANSARI",
        "Ebrahim Isa",
    ]
    statuses = [
        "In Design",
        "In GIS",
        "In Wayleave",
        "Completed",
        "Replan",
        "ReplanPassed",
        "Not Required",
    ]

    # Dictionary to store data for all engineers
    engineers_data = {}

    for engineer_name in engineer_names:
        # Get counts for each status
        status_counts = {
            status.replace(" ", "_"): depotcases2024.objects.filter(
                AREA_ENGINEER_NAME=engineer_name, PlanStatus=status
            ).count()
            for status in statuses
        }

        # Get total count for the engineer
        total_count = depotcases2024.objects.filter(
            AREA_ENGINEER_NAME=engineer_name
        ).count()

        # Store data for this engineer
        engineers_data[engineer_name] = {
            "total_count": total_count,
            "status_counts": status_counts,
        }

    return render(
        request,
        "dep24Rep.html",
        {
            "engineers_data": engineers_data,
            "is_admin": request.user.is_superuser,
        },
    )


def depot25Report(request):
    if not request.user.is_authenticated:
        return redirect("signin")

    engineer_names = [
        "A RAJESH",
        "Bassam",
        "MOHAMED RAJAB",
        "MOHAMED ALANSARI",
        "Ebrahim Isa",
    ]
    statuses = [
        "In Design",
        "In GIS",
        "In Wayleave",
        "Completed",
        "Replan",
        "ReplanPassed",
        "Not Required",
    ]

    # Dictionary to store data for all engineers
    engineers_data = {}

    for engineer_name in engineer_names:
        # Get counts for each status
        status_counts = {
            status.replace(" ", "_"): depotcases2025.objects.filter(
                AREA_ENGINEER_NAME=engineer_name, PlanStatus=status
            ).count()
            for status in statuses
        }

        # Get total count for the engineer
        total_count = depotcases2025.objects.filter(
            AREA_ENGINEER_NAME=engineer_name
        ).count()

        # Store data for this engineer
        engineers_data[engineer_name] = {
            "total_count": total_count,
            "status_counts": status_counts,
        }

    return render(
        request,
        "dep25Rep.html",
        {
            "engineers_data": engineers_data,
            "is_admin": request.user.is_superuser,
        },
    )


def loadReading2024Report(request):
    if not request.user.is_authenticated:
        return redirect("signin")

    # Fetch all records from the loadreading2025 model
    load_readings = LoadReading2024.objects.all()

    return render(
        request,
        "lr2024.html",
        {
            "load_readings": load_readings,
            "is_admin": request.user.is_superuser,
        },
    )


def view_case_dep_24(request, id):
    case = get_object_or_404(depotcases2024, id=id)
    context = {
        "case": case,
    }
    return render(request, "viewDet.html", context)


def view_case_dep_25(request, id):
    case = get_object_or_404(depotcases2025, id=id)
    context = {
        "case": case,
    }
    return render(request, "viewDet.html", context)

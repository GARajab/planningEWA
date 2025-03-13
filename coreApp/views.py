# accounts/views.py

import random
from typing import Collection
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import (
    depotcases2024,
    depotcases2025,
    Permit,
    loadreading2024,
    loadreading2025,
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
            messages.success(
                request, "Welcome " + username + " You Logged in successfully!"
            )
            return redirect("home")  # Use redirect instead of render
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("signin")

    return render(request, "signin.html")


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
            loadreading2024.objects.all()
        )  # Fetch all documents from the collection
        context = {
            "schemes": schemes,
            "is_admin": request.user.is_superuser,
        }
        return render(request, "Lreading24.html", context)
    else:
        return redirect("signin")


def lr25(request):
    if request.user.is_authenticated:
        schemes = (
            loadreading2025.objects.all()
        )  # Fetch all documents from the collection
        context = {
            "schemes": schemes,
            "is_admin": request.user.is_superuser,
        }
        return render(request, "Lreading25.html", context)
    else:
        return redirect("signin")


def nc24(request):
    if request.user.is_authenticated:
        permits = Permit.objects.all()
        context = {
            "permits": permits,
            "is_admin": request.user.is_superuser,
        }
        return render(
            request,
            "nc2024.html",
            context
        )
    else:
        return redirect("signin")


def edit_permit(request, permit_id):
    
    permit = get_object_or_404(Permit, id=permit_id)

    # Prepare permit data for JSON response
    permit_data = {
        "id": permit.id,
        "Number": permit.Number,
        "parcel_number": permit.parcel_number,
        "block": permit.block,
        "kw": permit.kw,
        "kva": permit.kva,
        "plan_status": permit.plan_status,
        "passed_date": permit.passed_date,
        "to_wl_date": permit.to_wl_date,
        "to_gis_date": permit.to_gis_date,
        "wl_number": permit.wl_number,
        "ref_no": permit.ref_no,
        "comment": permit.comment,
    }

    if request.method == "POST":
        # Collect data from request.POST and update the instance
        for field in permit._meta.get_fields():
            if field.name in request.POST:
                setattr(permit, field.name, request.POST[field.name])
        permit.save()
        messages.success(request, f"Permit {permit.Number} updated successfully!")
        return JsonResponse({"success": True})

    return JsonResponse(permit_data)


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
    load_readings = loadreading2024.objects.all()

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


def loadreading_detail_view(request, id):
    # Retrieve a specific record from the loadreading2024 model
    reading = get_object_or_404(loadreading2024, id=id)

    # Pass the data to the template
    return render(request, "veiwLR.html", {"reading": reading})


def delete_LR24(request, permit_id):
    if request.method == "POST":
        lr_del = get_object_or_404(loadreading2024, id=permit_id)
        lr_del.delete()
        messages.success(request, "Scheme " + lr_del.Sch_Ref + " Deleted Successfully.")
        return redirect("lr24")
    else:
        messages.error(request, "Invalid request Record Not Deleted.")
    return redirect("lr24")


def delete_LR25(request, permit_id):
    if request.method == "POST":
        lr_del = get_object_or_404(
            loadreading2024, id=permit_id
        )  # to be changed to loadreading25 if the table available and it is updated in model
        lr_del.delete()
        messages.success(request, "Scheme " + lr_del.Sch_Ref + " Deleted Successfully.")
        return redirect("lr25")
    else:
        messages.error(request, "Invalid request Record Not Deleted.")
    return redirect("lr25")


from django.shortcuts import render
from .models import depotcases2024, loadreading2024, depotcases2025, Permit
import random


def dashboard(request):
    # Fetch all cases for 2024
    cases_2024 = depotcases2024.objects.all()
    # Fetch all cases for 2025
    cases_2025 = depotcases2025.objects.all()
    # Fetch load readings for 2024
    load_readings_2024 = loadreading2024.objects.all()
    # Fetch permit data
    permits = Permit.objects.all()

    # Prepare data for Chart.js for 2024
    engineers_2024 = (
        cases_2024.values("AREA_ENGINEER_NAME")
        .distinct()
        .order_by("AREA_ENGINEER_NAME")
    )
    statuses_2024 = cases_2024.values("PlanStatus").distinct().order_by("PlanStatus")

    data_2024 = {
        engineer["AREA_ENGINEER_NAME"]: {
            status["PlanStatus"]: 0 for status in statuses_2024
        }
        for engineer in engineers_2024
    }

    for case in cases_2024:
        engineer_name = case.AREA_ENGINEER_NAME
        plan_status = case.PlanStatus
        if engineer_name and plan_status:
            data_2024[engineer_name][plan_status] += 1

    labels_2024 = [engineer for engineer in data_2024.keys()]
    datasets_2024 = []

    for status in statuses_2024:
        status_label = (
            status["PlanStatus"] if status["PlanStatus"] is not None else "Unknown"
        )
        dataset = {
            "label": status_label,
            "data": [
                data_2024[engineer].get(status_label, 0) for engineer in labels_2024
            ],
            "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.2)",
            "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)",
            "borderWidth": 1,
        }
        datasets_2024.append(dataset)

    total_records_2024 = cases_2024.count()

    # Prepare data for Chart.js for 2025
    engineers_2025 = (
        cases_2025.values("AREA_ENGINEER_NAME")
        .distinct()
        .order_by("AREA_ENGINEER_NAME")
    )
    statuses_2025 = cases_2025.values("PlanStatus").distinct().order_by("PlanStatus")

    data_2025 = {
        engineer["AREA_ENGINEER_NAME"]: {
            status["PlanStatus"]: 0 for status in statuses_2025
        }
        for engineer in engineers_2025
    }

    for case in cases_2025:
        engineer_name = case.AREA_ENGINEER_NAME
        plan_status = case.PlanStatus
        if engineer_name and plan_status:
            data_2025[engineer_name][plan_status] += 1

    labels_2025 = [engineer for engineer in data_2025.keys()]
    datasets_2025 = []

    for status in statuses_2025:
        status_label = (
            status["PlanStatus"] if status["PlanStatus"] is not None else "Unknown"
        )
        dataset = {
            "label": status_label,
            "data": [
                data_2025[engineer].get(status_label, 0) for engineer in labels_2025
            ],
            "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.2)",
            "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)",
            "borderWidth": 1,
        }
        datasets_2025.append(dataset)

    total_records_2025 = cases_2025.count()

    # Prepare data for Chart.js for Load Readings 2024
    engineers_load_2024 = (
        load_readings_2024.values("PlanEng").distinct().order_by("PlanEng")
    )
    statuses_load_2024 = (
        load_readings_2024.values("Plan_Status").distinct().order_by("Plan_Status")
    )

    data_load_2024 = {
        engineer["PlanEng"]: {status["Plan_Status"]: 0 for status in statuses_load_2024}
        for engineer in engineers_load_2024
    }

    for case in load_readings_2024:
        engineer_name = case.PlanEng
        plan_status = case.Plan_Status
        if engineer_name and plan_status:
            data_load_2024[engineer_name][plan_status] += 1

    labels_load_2024 = [engineer for engineer in data_load_2024.keys()]
    datasets_load_2024 = []

    for status in statuses_load_2024:
        status_label = (
            status["Plan_Status"] if status["Plan_Status"] is not None else "Unknown"
        )
        dataset = {
            "label": status_label,
            "data": [
                data_load_2024[engineer].get(status_label, 0)
                for engineer in labels_load_2024
            ],
            "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.2)",
            "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)",
            "borderWidth": 1,
        }
        datasets_load_2024.append(dataset)

    total_records_load_2024 = load_readings_2024.count()

    # Prepare data for Chart.js for Permits
    engineers_permits = permits.values("planeng").distinct().order_by("planeng")
    statuses_permits = permits.values("plan_status").distinct().order_by("plan_status")

    data_permits = {
        engineer["planeng"]: {status["plan_status"]: 0 for status in statuses_permits}
        for engineer in engineers_permits
    }

    for case in permits:
        engineer_name = case.planeng
        plan_status = case.plan_status
        if engineer_name and plan_status:
            data_permits[engineer_name][plan_status] += 1

    labels_permits = [engineer for engineer in data_permits.keys()]
    datasets_permits = []

    for status in statuses_permits:
        status_label = (
            status["plan_status"] if status["plan_status"] is not None else "Unknown"
        )
        dataset = {
            "label": status_label,
            "data": [
                data_permits[engineer].get(status_label, 0)
                for engineer in labels_permits
            ],
            "backgroundColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 0.2)",
            "borderColor": f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)",
            "borderWidth": 1,
        }
        datasets_permits.append(dataset)

    total_records_permits = permits.count()

    # Prepare context for the template
    context = {
        "labels_2024": labels_2024,
        "datasets_2024": datasets_2024,
        "total_records_2024": total_records_2024,
        "labels_2025": labels_2025,
        "datasets_2025": datasets_2025,
        "total_records_2025": total_records_2025,
        "labels_load_2024": labels_load_2024,
        "datasets_load_2024": datasets_load_2024,
        "total_records_load_2024": total_records_load_2024,
        "labels_permits": labels_permits,
        "datasets_permits": datasets_permits,
        "total_records_permits": total_records_permits,
    }

    return render(request, "dashboard.html", context)


def fetch_scheme_references(request):
    label = request.GET.get("label")
    status = request.GET.get("status")
    table = request.GET.get("table")
    scheme_references = []

    if table == "depotcases2024":
        scheme_references = list(
            depotcases2024.objects.filter(
                AREA_ENGINEER_NAME=label, PlanStatus=status
            ).values_list("REFRENCENUMBER", flat=True)
        )
    elif table == "depotcases2025":
        scheme_references = list(
            depotcases2025.objects.filter(
                AREA_ENGINEER_NAME=label, PlanStatus=status
            ).values_list("REFRENCENUMBER", flat=True)
        )
    elif table == "loadreading2024":
        scheme_references = list(
            loadreading2024.objects.filter(
                PlanEng=label, Plan_Status=status
            ).values_list("Sch_Ref", flat=True)
        )
    elif table == "permits":
        scheme_references = list(
            Permit.objects.filter(planeng=label, plan_status=status).values_list(
                "Number", flat=True
            )
        )

    return JsonResponse({"schemeReferences": scheme_references})


def update_LR24(request, id):
    case = get_object_or_404(loadreading2024, id=id)

    if request.method == "POST":
        for field in case._meta.get_fields():
            if field.name in request.POST:
                value = request.POST[field.name]
                if value == "":
                    value = None
                setattr(case, field.name, value)
        case.save()
        messages.success(request, f"Scheme {case.Sch_Ref} is updated successfully!")
        return JsonResponse({"success": True})
    else:
        case_data = {
            "id": case.id,
            "Sch_Ref": case.Sch_Ref,
            "PlanEng": case.PlanEng,
            "BLOCK": case.BLOCK,
            "SSNO": case.SSNO,
            "TXNO": case.TXNO,
            "LVB_FDR": case.LVB_FDR,
            "KVA": case.KVA,
            "WL_NO": case.WL_NO,
            "USPDATE": case.USPDATE,
            "passed_date": case.passed_date,
            "Plan_Status": case.Plan_Status,
            "CONST_COMP": case.CONST_COMP,
            "Labour": case.Labour,
            "Material": case.Material,
            "cable_length": case.cable_length,
            "totalcost": case.totalcost,
            "GISDATE": case.GISDATE,
            "RCCDATE": case.RCCDATE,
            "MSPDATE": case.MSPDATE,
        }

    if request.method == "POST":
        # Collect data from request.POST and update the instance
        for field in case._meta.get_fields():
            if field.name in request.POST:
                setattr(case, field.name, request.POST[field.name])
        case.save()
        messages.success(
            request, "Scheme " + case.Sch_Ref + " is updated successfully!"
        )
        return JsonResponse({"success": True})
    return JsonResponse(case_data)


def view_case_nc(request, id):
    case = get_object_or_404(Permit, id=id)
    context = {
        "case": case,
    }
    return render(request, "viewNC.py.html", context)


def LR24Report(request):
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
            status.replace(" ", "_"): loadreading2024.objects.filter(
                PlanEng=engineer_name, Plan_Status=status
            ).count()
            for status in statuses
        }

        # Get total count for the engineer
        total_count = loadreading2024.objects.filter(
            PlanEng=engineer_name
        ).count()

        # Store data for this engineer
        engineers_data[engineer_name] = {
            "total_count": total_count,
            "status_counts": status_counts,
        }

    return render(
        request,
        "LR2024Rep.py.html",
        {
            "engineers_data": engineers_data,
            "is_admin": request.user.is_superuser,
        },
    )
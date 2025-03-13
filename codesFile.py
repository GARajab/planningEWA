<span style="font-size: 12px;"
            class="{% if scheme.PlanStatus == 'Completed' %}badge badge-success rounded-pill d-inline{% elif scheme.PlanStatus == 'In GIS' %}badge badge-primary rounded-pill d-inline{% elif scheme.PlanStatus == 'In Wayleave' %}badge badge-warning rounded-pill d-inline{% elif scheme.PlanStatus == 'Not Required' %}badge badge-info rounded-pill d-inline{% elif scheme.PlanStatus == 'In Design' %}badge badge-danger rounded-pill d-inline{% endif %}">
            
          </span>



 <div class="form-group">
              <label for="PlanStatus">Plan Status</label>
              <select class="form-select" id="PlanStatus" name="PlanStatus">
                <option value="In Design">In Design</option>
                <option value="Completed">Completed</option>
                <option value="In GIS">In GIS</option>
                <option value="In Wayleave">In Wayleave</option>
                <option value="Not Required">Not Required</option>
              </select>
            </div>



if request.method == "POST":
        # Get the data from the request
        uspdate = request.POST.get("USPDATE")
        passeddate = request.POST.get("PASSEDDATE")
        gisdate = request.POST.get("GISDATE")
        rccdate = request.POST.get("RCCDATE")
        mspdate = request.POST.get("MSPDATE")
        labourcost = request.POST.get("labourcost")
        ministrycost = request.POST.get("ministrycost")
        cable_length = request.POST.get("cable_length")
        noOfServ = request.POST.get("noOfServ")
        noOfFaults = request.POST.get("noOfFaults")
        totalcost = request.POST.get("totalcost")

        # Convert empty strings to None
        uspdate = None if uspdate == "" else uspdate
        passeddate = None if passeddate == "" else passeddate
        gisdate = None if gisdate == "" else gisdate
        rccdate = None if rccdate == "" else rccdate
        mspdate = None if mspdate == "" else mspdate

        labourcost = None if labourcost == "" else float(labourcost)
        ministrycost = None if ministrycost == "" else float(ministrycost)
        cable_length = None if cable_length == "" else float(cable_length)
        noOfServ = None if noOfServ == "" else float(noOfServ)
        noOfFaults = None if noOfFaults == "" else float(noOfFaults)
        totalcost = None if totalcost == "" else float(totalcost)

        # Create or update the model instance
        depot_case = depotcases2024(
            USPDATE=uspdate,
            PASSEDDATE=passeddate,
            GISDATE=gisdate,
            RCCDATE=rccdate,
            MSPDATE=mspdate,
            labourcost=labourcost,
            ministrycost=ministrycost,
            cable_length=cable_length,
            noOfServ=noOfServ,
            noOfFaults=noOfFaults,
            totalcost=totalcost,
            # Add other fields here
        )
        depot_case.save()



          <!-- Scripts -->
  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/pdfmake.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.2.7/vfs_fonts.js"></script>


  <p class="fw-normal mb-1">
            {% if engineer_name == "A RAJESH" %}
            Area <br> 1 + 2 + 9
            {% elif engineer_name == "Bassam" %}
            Area <br> 3 + 12
            {% elif engineer_name == "MOHAMED RAJAB" %}
            Area <br> 4 + 5
            {% elif engineer_name == "MOHAMED ALANSARI" %}
            Area <br> 6 + 7 + 8
            {% elif engineer_name == "Ebrahim Isa" %}
            Area <br> 10
            {% endif %}
          </p>





 <form id="myForm_{{ scheme.id }}" action="{% url 'delete_depot24' scheme.id %}" method="POST"
            style="display:inline;">
            {% csrf_token %}
            <input type="hidden" id="recordId_{{ scheme.id }}" name="recordId" value="{{ scheme.id }}">
            <a href="javascript:void(0);" onclick="submitForm('{{ scheme.id }}')"><i class="fas fa-trash"
                style="text-decoration: none;font-size: 20px; color: #f88498; padding: 10px; display: inline-block;"></i></a>
          </form>






  <link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/8.1.0/mdb.min.css" rel="stylesheet" />



  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
  <!-- Popper.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/datatables/1.10.21/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/datatables.net@2.2.2/js/dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/2.2.2/js/dataTables.bootstrap5.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.8/umd/popper.min.js"></script>
  <!-- MDB UI Kit -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/8.1.0/mdb.umd.min.js"></script>
  <!-- Font Awesome -->




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
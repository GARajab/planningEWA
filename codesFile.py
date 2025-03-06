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
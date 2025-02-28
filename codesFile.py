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
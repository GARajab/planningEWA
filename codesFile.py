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
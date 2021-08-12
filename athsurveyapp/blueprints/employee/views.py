from flask import Blueprint, render_template, redirect, url_for, request
from athsurveyapp.blueprints.employee.forms import EmployeeForm
from athsurveyapp.models.models import Employee, Branch, Question, db
import datetime

employee_page = Blueprint('employee_page', __name__,
                          template_folder="templates")


@employee_page.route("/")
def employee_index():

    employees = Employee.query.all()

    return render_template('employees.html', employees=employees)

@employee_page.route("/<id>", methods=['GET', 'POST'])
def employee_details(id):
    form = EmployeeForm()
    
    if request.method == "POST" and form.validate_on_submit():
            
        employee_to_edit = Employee.query.get(form.id.data)
        
        employee_to_edit.name = form.name.data
        employee_to_edit.code = form.code.data
        employee_to_edit.designation = form.designation.data
        employee_to_edit.branch = form.branch.data
        employee_to_edit.gender = form.gender.data
        
        db.session.commit()
    
    employee = Employee.query.get(id)
    
    for resp in employee.responses:
        print(resp.date_created)
        setattr(resp, "response_date", resp.date_created.strftime('%m/%d/%Y'))
        
        score = 0
        
        for ques_res in resp.question_responses:
            score += int(ques_res.answer)
            setattr(resp, "average", score / len(resp.question_responses))
    
    form.id.default = employee.id
    form.name.default = employee.name
    form.branch.default = employee.branch
    form.code.default = employee.code
    form.designation.default = employee.designation
    form.gender.default = employee.gender
    form.process()
    
    return render_template('employee_details.html', employee=employee, form=form)
    


@employee_page.route("/create", methods=['GET', 'POST'])
def create_employee():

    form = EmployeeForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        emp_name = form.name.data
        emp_code = form.code.data
        emp_designation = form.designation.data
        emp_branch = form.branch.data.id
        emp_gender = form.gender.data
        

        new_emp = Employee(emp_name, emp_code, emp_designation, emp_branch, emp_gender)

        db.session.add(new_emp)
        db.session.commit()

        return redirect(url_for('employee_page.employee_details', id=new_emp.id))

    return render_template('create_employee.html', form=form)

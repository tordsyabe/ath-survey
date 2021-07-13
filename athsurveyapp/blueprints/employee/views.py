from flask import Blueprint, render_template, redirect, url_for, request
from athsurveyapp.blueprints.employee.forms import EmployeeForm
from athsurveyapp.models.models import Employee, Branch, db

employee_page = Blueprint('employee_page', __name__,
                          template_folder="templates")


@employee_page.route("/")
def employee_index():

    employees = Employee.query.all()

    return render_template('employees.html', employees=employees)


@employee_page.route("/create", methods=['GET', 'POST'])
def create_employee():

    form = EmployeeForm()
    if request.method == 'POST' and form.validate_on_submit():
        emp_name = form.name.data
        emp_code = form.code.data
        emp_designation = form.designation.data
        emp_branch = form.branch.data.id

        new_emp = Employee(emp_name, emp_code, emp_designation, emp_branch)

        db.session.add(new_emp)
        db.session.commit()

        return redirect(url_for('employee_page.employee_index'))

    return render_template('create_employee.html', form=form)

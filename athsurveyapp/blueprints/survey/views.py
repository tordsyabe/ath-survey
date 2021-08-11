from athsurveyapp.blueprints import employee
from flask import Blueprint, render_template, request, redirect, url_for
from athsurveyapp.blueprints.survey.forms import SurveyForm, ConductSurveyForm
from athsurveyapp.blueprints.question.forms import QuestionForm
from athsurveyapp.models.models import db, Survey, Branch, Employee, Response, QuestionResponse, Question

from athsurveyapp.blueprints.question_type import QuestionTypeForm

survey_page = Blueprint("survey_page", __name__, template_folder="templates")


@survey_page.route("/", methods=["GET"])
def survey_index():

    surveys = Survey.query.all()

    return render_template("surveys.html", surveys=surveys)


@survey_page.route("/create", methods=["GET", "POST"])
def create_survey():
    form = SurveyForm()

    if request.method == "POST" and form.validate_on_submit():
        survey_name = form.name.data
        survey_desc = form.description.data

        new_survey = Survey(survey_name, survey_desc)

        db.session.add(new_survey)
        db.session.commit()
        print(new_survey)

        return redirect(url_for("survey_page.survey_index"))

    return render_template("create_survey.html", form=form)


@survey_page.route("/<id>")
def survey_details(id):

    qt_form = QuestionTypeForm()
    question_form = QuestionForm()
    survey = Survey.query.get(id)
    print(survey)

    return render_template(
        "survey_details.html",
        survey=survey,
        qt_form=qt_form,
        question_form=question_form,
    )
    
@survey_page.route("/conduct", methods=["GET", "POST"])
def conduct_survey():
    
    url_employee_id = request.args.get('employee')
    url_branch_id = request.args.get('branch')
    
    form = ConductSurveyForm()
    
    if url_branch_id and url_employee_id:
        default_branch = Branch.query.get(url_branch_id)
        default_emp = Employee.query.get(url_employee_id)

        form.branch.default = default_branch
        form.employee.default = default_emp
        
        form.process()

    # form.employee.default = url_employee_id
    
    branches = Branch.query.all()
    
    if url_branch_id:
        employees = Employee.query.filter_by(branch_id=url_branch_id)
    else:
        employees = Employee.query.filter_by(branch_id=1)
        
    survey = Survey.query.get(1)
    
    if request.method == "POST":
        employee = request.form["employee"]
        survey = request.form["survey"]
        
        new_response = Response(employee, survey)
        feedback = []
        
        question_responses = [[fieldname, value] for fieldname, value in request.form.items()]
        for index, feedbacks in enumerate(question_responses):
            
            if index > 3:
                if index % 2 == 1:
                    feedback.append(feedbacks[1])
        # print(feedback)
        f = 0
        for idx, answers in enumerate(question_responses):
            
            if idx > 3:
                if idx % 2 == 0:
                    question_desc = Question.query.get(answers[0])
                    new_response.question_responses.append(QuestionResponse(question_desc.description, answers[0], answers[1], feedback[f]))
                    f += 1
                    
        db.session.add(new_response)
        db.session.commit()
        
        return redirect(url_for("employee_page.employee_details", id=employee))
    
    return render_template("conduct_survey.html", form=form, branches=branches, employees=employees, survey=survey)

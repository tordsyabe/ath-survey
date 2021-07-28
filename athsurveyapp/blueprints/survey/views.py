from flask import Blueprint, render_template, request, redirect, url_for
from athsurveyapp.blueprints.survey.forms import SurveyForm, ConductSurveyForm
from athsurveyapp.blueprints.question.forms import QuestionForm
from athsurveyapp.models.models import db, Survey, Branch

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
    
    form = ConductSurveyForm()
    
    data = request.form
    
    branches = Branch.query.all()
    
    print(data)
    
    return render_template("conduct_survey.html", form=form, branches=branches)

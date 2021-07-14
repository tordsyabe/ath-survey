from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from athsurveyapp.blueprints.question.forms import QuestionForm

questions_page = Blueprint('questions_page', __name__, template_folder='templates')

@questions_page.route('/questions', methods=['POST'])
def create_questions():
    
    form = QuestionForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        desc = form.description.data
        is_req = form.is_required.data
        place_num = form.place_number.data
        ques_type = form.question_type.data.id
        choice = form.choice.data.id
        survey = form.survey.data.id            
    return jsonify({"good": "job!"})
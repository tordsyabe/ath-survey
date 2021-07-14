from flask import Blueprint, render_template, request, redirect, url_for, jsonify

questions_page = Blueprint('questions_page', __name__, template_folder='templates')

@questions_page.route('/questions', methods=['POST'])
def create_questions():
    
    return jsonify({"good": "job!"})
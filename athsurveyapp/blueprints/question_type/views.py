from flask import Blueprint

question_type_page = Blueprint(
    "question_type_page", __name__, template_folder="templates"
)

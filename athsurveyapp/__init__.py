from flask import Flask
from athsurveyapp.models.models import db, User
from flask_migrate import Migrate
from flask_restful import Api
from flask_login import LoginManager 

import os

from athsurveyapp.blueprints.dashboard import dashboard_page
from athsurveyapp.blueprints.survey import survey_page, SurveyResource
from athsurveyapp.blueprints.branch import branch_page
from athsurveyapp.blueprints.employee import employee_page, EmployeeResourceList, BranchEmployeeResource, EmployeeResource, EmployeeResponseResource
from athsurveyapp.blueprints.question_type import (
    question_type_page,
    QuestionTypeResource,
    QuestionTypeResourceList,
)
from athsurveyapp.blueprints.question import (
    question_page,
    QuestionResouce,
    QuestionResourceList,
)
from athsurveyapp.schemas import ma

from athsurveyapp.blueprints.auth import auth_page

migrate = Migrate()
api = Api()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SECRET_KEY"] = "secrettalagato"
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth_page.login'
    login_manager.login_message_category = "danger"
    login_manager.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.environ.get("DB_USER")}:{os.environ.get("DB_PASSWORD")}@{os.environ.get("DB_HOST")}:5432/{os.environ.get("DB_NAME")}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    api.add_resource(QuestionTypeResource, "/api/question_types/<int:id>")
    api.add_resource(QuestionTypeResourceList, "/api/question_types")

    api.add_resource(QuestionResouce, "/api/questions/<int:id>")
    api.add_resource(QuestionResourceList, "/api/questions")

    api.add_resource(SurveyResource, "/api/surveys/<int:id>")
    
    api.add_resource(EmployeeResourceList, "/api/employees")
    api.add_resource(EmployeeResource, "/api/employees/<int:id>")
    api.add_resource(BranchEmployeeResource, "/api/employees/branch/<int:id>")
    api.add_resource(EmployeeResponseResource, "/api/employees/responses/<int:id>")

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    ma.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    
    from athsurveyapp.models.models import Employee, Branch

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    app.register_blueprint(dashboard_page, url_prefix="/")
    app.register_blueprint(survey_page, url_prefix="/surveys")
    app.register_blueprint(branch_page, url_prefix="/branches")
    app.register_blueprint(employee_page, url_prefix="/employees")
    app.register_blueprint(auth_page)

    return app

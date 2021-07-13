from flask import Flask, blueprints
from athsurveyapp.models.models import db
from flask_migrate import Migrate
import os

from athsurveyapp.blueprints.survey import survey_page
from athsurveyapp.blueprints.branch import branch_page
from athsurveyapp.blueprints.employee import employee_page

migrate = Migrate()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SECRET_KEY"] = 'secrettalagato'

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + \
        os.path.join(basedir, 'data.sqlite')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    from athsurveyapp.models.models import Employee, Branch

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    app.register_blueprint(survey_page, url_prefix='/surveys')
    app.register_blueprint(branch_page, url_prefix='/branches')
    app.register_blueprint(employee_page, url_prefix='/employees')

    return app

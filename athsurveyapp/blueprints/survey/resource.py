from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask_login import login_required
from athsurveyapp.decorators import admin_required

from athsurveyapp.models.models import Survey, db
from athsurveyapp.schemas import SurveySchema

survey_args = reqparse.RequestParser()
survey_args.add_argument(
    "name", type=str, help="Survey name is required", required=True
)
survey_args.add_argument(
    "description", type=str, help="Survey description is required", required=True
)


class SurveyResource(Resource):
    decorators = [login_required, admin_required]
    def get(self, id):
        survey = Survey.query.get(id)
        
        if not survey:
            abort(400, message="Survey does not exist")
        
        survey_schema = SurveySchema()
        
        return survey_schema.dump(survey)
    
    def put(self, id):
        args = survey_args.parse_args()
        survey_to_update = Survey.query.get(id)

        if not survey_to_update:
            abort(400, message="Survey does not exist")

        survey_to_update.name = args["name"]
        survey_to_update.description = args["description"]

        db.session.commit()
        updated_survey_schame = SurveySchema()
        return updated_survey_schame.dump(survey_to_update), 200

    def delete(self, id):

        survey = Survey.query.get(id)

        if not survey:
            abort(400, message="Survey does not exists")

        db.session.delete(survey)
        db.session.commit()

        return {"message": "Survey successfully deleted"}, 200

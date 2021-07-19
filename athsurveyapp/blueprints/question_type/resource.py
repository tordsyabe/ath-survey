from flask_restful import Resource, reqparse, abort
from flask import jsonify

from athsurveyapp.models.models import QuestionType as Qt, db
from athsurveyapp.schemas import QtSchema

question_type_args = reqparse.RequestParser()
question_type_args.add_argument(
    "description", type=str, help="Survey category description", required=True
)
question_type_args.add_argument("survey_id", type=int, help="Survey", required=True)


class QuestionTypeResource(Resource):
    def get(self, id):

        question_type = Qt.query.get(id)

        if not question_type:
            abort(400, message="Category does not exist")

        qt_schema = QtSchema()

        return qt_schema.dump(question_type)

    def put(self, id):
        args = question_type_args.parse_args()
        qt_to_update = Qt.query.get(id)

        if not qt_to_update:
            abort(400, message="Category does not exist")

        qt_to_update.description = args["description"]
        qt_to_update.survey_id = args["survey_id"]

        db.session.commit()
        schema = QtSchema()
        return schema.dump(qt_to_update), 200

    def delete(self, id):
        qt_to_delete = Qt.query.get(id)

        if not qt_to_delete:
            abort(400, message="Category does not exist")

        db.session.delete(qt_to_delete)
        db.session.commit()
        return {"message": "Question type successfully deleted"}, 200


class QuestionTypeResourceList(Resource):
    def get(self):

        question_types = Qt.query.all()

        qts_schema = QtSchema(many=True)

        return qts_schema.dump(question_types)

    def post(self):

        args = question_type_args.parse_args()

        new_question_type = Qt(args["description"], args["survey_id"])

        db.session.add(new_question_type)
        db.session.commit()

        new_qt_schema = QtSchema()

        return new_qt_schema.dump(new_question_type), 201

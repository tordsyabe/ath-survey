from flask_restful import Resource
from flask import jsonify

from athsurveyapp.models.models import QuestionType as Qt, db
from athsurveyapp.schemas import QtSchema
class QuestionTypeResource(Resource):
    def get(self):
        
        question_type = Qt.query.get(2)
        print(question_type)
        
        schema = QtSchema()
        
        return schema.dump(question_type)
    
    
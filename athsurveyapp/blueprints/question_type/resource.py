from flask_restful import Resource, reqparse
from flask import jsonify

from athsurveyapp.models.models import QuestionType as Qt, db
from athsurveyapp.schemas import QtSchema




class QuestionTypeResource(Resource):
    def get(self, id):
        
        question_type = Qt.query.get(id)
        print(question_type)
        
        schema = QtSchema()
        
        return schema.dump(question_type)
    
    def put(self):
        pass
    
    
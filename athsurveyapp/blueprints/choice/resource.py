from flask_restful import Resource
from flask import jsonify
from flask_login import login_required

class ChoiceResourceList(Resource):
    decorators = [login_required]
    def post(self, id):
        pass
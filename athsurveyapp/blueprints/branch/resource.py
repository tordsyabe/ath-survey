from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask_login import login_required

from athsurveyapp.models.models import Branch, db

class BranchResource(Resource):
    decorators = [login_required]
    def delete(self, id):
        
        branch_to_delete = Branch.query.get(id)
        
        if not branch_to_delete:
            abort(404, message="Branch does not exist")
        
        db.session.delete(branch_to_delete)
        db.session.commit()
        
        return {"message": "Branch successfully deleted"}
    
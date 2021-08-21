from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask_login import login_required
from athsurveyapp.decorators import admin_required

from athsurveyapp.models.models import Employee, Response, db
from athsurveyapp.schemas import EmployeeSchema, EmployeeByBranchSchema, ResponseSchema



class BranchEmployeeResource(Resource):
    decorators = [login_required]
    def get(self, id):
        
        employees_by_branch = Employee.query.filter_by(branch_id=id) 
        employees_by_branch_schema = EmployeeByBranchSchema(many=True)
        return employees_by_branch_schema.dump(employees_by_branch)
    
class EmployeeResource(Resource):
    decorators = [login_required, admin_required]
    def get(self, id):
        
        employee = Employee.query.get(id)
        
        if not employee:
            abort(404, message="Employee does not exist")
            
            
        employee_schema = EmployeeSchema()
            
        return employee_schema.dump(employee)
    
    def delete(self, id):
        
        employee_to_delete = Employee.query.get(id)
        
        if not employee_to_delete:
            abort(404, message="Employee does not exist")
        
        db.session.delete(employee_to_delete)
        db.session.commit()
        
        return {"message": "Employee successfully deleted"}

class EmployeeResourceList(Resource):
    decorators = [login_required, admin_required]
    def get(self):
        employees = Employee.query.all()
        
        employee_list_schema = EmployeeSchema(many=True)
        
        return employee_list_schema.dump(employees)
    
class EmployeeResponseResource(Resource):
    decorators = [login_required, admin_required]
    def get(self, id):
        
        response = Response.query.get(id)
        
        if not response:
            abort(404, message="Response does not exist")
            
        response_schema = ResponseSchema()
        
        return response_schema.dump(response)
    
    def delete(self, id):
        
        response_to_delete = Response.query.get(id)
        
        if not response_to_delete:
            abort(404, message="Response does not exist")
        
        db.session.delete(response_to_delete)
        db.session.commit()
        
        return {"message": "Response successfully deleted"}
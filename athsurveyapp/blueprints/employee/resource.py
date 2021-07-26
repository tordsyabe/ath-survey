from flask_restful import Resource, reqparse, abort
from flask import jsonify

from athsurveyapp.models.models import Employee, db
from athsurveyapp.schemas import EmployeeSchema, EmployeeByBranchSchema



class BranchEmployeeResource(Resource):
    
    def get(self, id):
        
        employees_by_branch = Employee.query.filter_by(branch_id=id) 
        employees_by_branch_schema = EmployeeByBranchSchema(many=True)
        return employees_by_branch_schema.dump(employees_by_branch)
    
class EmployeeResource(Resource):
    
    def get(self, id):
        
        employee = Employee.query.get(id)
        
        if not employee:
            abort(404, message="Employee does not exist")
            
            
        employee_schema = EmployeeSchema()
            
        return employee_schema.dump(employee)

class EmployeeResourceList(Resource):
    
    def get(self):
        employees = Employee.query.all()
        
        employee_list_schema = EmployeeSchema(many=True)
        
        return employee_list_schema.dump(employees)
    
    
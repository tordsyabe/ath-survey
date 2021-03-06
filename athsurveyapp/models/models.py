from sqlalchemy.sql import func
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(254))
    name = db.Column(db.String(64))
    is_admin = db.Column(db.Boolean, default=False)

class Employee(db.Model):

    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(15), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    designation = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey("branch.id"), nullable=False)
    name = db.Column(db.String(254), nullable=False)
    code = db.Column(db.String(254), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    designation = db.Column(db.String(254), nullable=False)
    
    responses = db.relationship("Response", backref="employee", cascade="all, delete-orphan")

    def __init__(self, name, code, designation, branch_id, gender):
        self.name = name
        self.code = code
        self.designation = designation
        self.branch_id = branch_id
        self.gender = gender


class Branch(db.Model):

    __tablename__ = "branch"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    address = db.Column(db.String(120))
    name = db.Column(db.String(254), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    address = db.Column(db.String(254))
    employees = db.relationship("Employee", backref="branch")

    def __init__(self, name, address):
        self.name = name
        self.address = address


class Survey(db.Model):

    __tablename__ = "survey"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    question_types = db.relationship("QuestionType", backref="survey", cascade="all, delete-orphan", order_by="QuestionType.sequence")

    def __init__(self, name, description):
        self.name = name
        self.description = description


class QuestionType(db.Model):

    __tablename__ = "question_type"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"), nullable=False)
    sequence = db.Column(db.Integer)

    questions = db.relationship("Question", backref="question_type", cascade="all, delete-orphan", order_by="Question.sequence")

    def __init__(self, description, survey_id, sequence):
        self.description = description
        self.survey_id = survey_id
        self.sequence = sequence


class Question(db.Model):

    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    is_required = db.Column(db.Boolean, nullable=False, default=False)
    sequence = db.Column(db.Integer, nullable=False)

    question_type_id = db.Column(db.Integer, db.ForeignKey("question_type.id"), nullable=False)
    choice_id = db.Column(db.Integer, db.ForeignKey("choice.id"), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __init__(self,description, is_required, sequence, question_type_id, choice_id):
        self.description = description
        self.is_required = is_required
        self.sequence = sequence
        self.question_type_id = question_type_id
        self.choice_id = choice_id


class Choice(db.Model):

    __tablename__ = "choice"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Integer)

    questions = db.relationship("Question", backref="choice")
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __init__(self, description, value):
        self.description = description
        self.value = value

class Response(db.Model):

    __tablename__ = "response"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=False)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    question_responses = db.relationship("QuestionResponse", backref="response", cascade="all, delete-orphan")
    survey = db.relationship("Survey", backref="responses")
    user = db.relationship("User", backref="responses")

    def __init__(self, employee_id, survey_id, user_id):
        self.employee_id = employee_id
        self.survey_id = survey_id
        self.user_id = user_id


class QuestionResponse(db.Model):

    __tablename__ = "question_response"

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(254))
    feedback = db.Column(db.String(254))
    response_id = db.Column(db.Integer, db.ForeignKey("response.id"), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    question = db.Column(db.String(254))
    
    def __init__(self, question, question_id, answer, feedback):
        self.question = question
        self.question_id = question_id
        self.answer = answer
        self.feedback = feedback

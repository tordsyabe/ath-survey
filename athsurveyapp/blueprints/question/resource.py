from flask_restful import Resource, reqparse, abort
from flask import jsonify
from flask_login import login_required


from athsurveyapp.models.models import Question, db
from athsurveyapp.schemas import QuestionSchema

question_args = reqparse.RequestParser()

question_args.add_argument("id")
question_args.add_argument(
    "description", type=str, help="Question description is required", required=True
)

question_args.add_argument(
    "sequence", type=int, help="Question sequence number", required=True
)
question_args.add_argument(
    "choice_id", type=int, help="Question choice is required", required=True
)

question_args.add_argument(
    "is_required",
    type=bool,
    help="Question is required",
)

question_args.add_argument(
    "question_type_id",
    type=int,
    help="Question type is required",
)


class QuestionResouce(Resource):
    decorators = [login_required]
    def get(self, id):
        question = Question.query.get(id)

        if not question:
            abort(400, message="Question does not exist")

        question_schema = QuestionSchema()

        return question_schema.dump(question)
    
    def delete(self, id):

        question = Question.query.get(id)

        if not question:
            abort(400, message="Questio does not exist")

        db.session.delete(question)
        db.session.commit()

        return {"message": "Question successfully deleted"}, 200


class QuestionResourceList(Resource):
    decorators = [login_required]
    def get(self):
        questions = Question.query.all()

        questions_schema = QuestionSchema(many=True)

        return questions_schema.dump(questions)

    def post(self):

        args = question_args.parse_args()

        question_schema = QuestionSchema()


        if args["id"]:
            question = Question.query.get(int(args["id"]))

            question.description = args["description"]
            question.choice_id = args["choice_id"]
            question.question_type_id = args["question_type_id"]
            question.sequence = args["sequence"]
            question.is_required = args["is_required"]

            db.session.commit()

            return question_schema.dump(question), 201

        new_question = Question(
            args["description"],
            args["is_required"],
            args["sequence"],
            args["question_type_id"],
            args["choice_id"],
        )

        db.session.add(new_question)
        db.session.commit()


        return question_schema.dump(new_question), 201

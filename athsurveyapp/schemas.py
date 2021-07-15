from flask_marshmallow import Marshmallow

ma = Marshmallow()

class QtSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "description")
import marshmallow
from flask_marshmallow import Schema


class DefaultHealthResponseSchema(Schema):
    message = marshmallow.fields.String()


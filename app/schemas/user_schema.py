from app import ma
from app.models import User


class UserSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        model = User

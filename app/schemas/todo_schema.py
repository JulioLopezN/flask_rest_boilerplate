from app import ma
from app.models import Todo


class TodoSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        model = Todo

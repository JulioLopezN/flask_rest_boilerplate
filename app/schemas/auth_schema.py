from app import ma


class LoginSchema(ma.Schema):
    username = ma.String()
    password = ma.String()
    remember_me = ma.Boolean()
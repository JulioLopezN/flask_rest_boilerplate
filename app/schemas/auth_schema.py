from app import ma


class LoginSchema(ma.Schema):
    email = ma.String()
    password = ma.String()
    remember_me = ma.Boolean()
    
class RegisterSchema(ma.Schema):
    email = ma.Email()
    first_name = ma.String()
    last_name = ma.String()
    password = ma.String()
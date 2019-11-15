from functools import wraps
from flask import g, request

def authorized(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if g.user is None:
                return {'error': 'Unauthorize'}, 401
            elif role is not None and role not in g.user.roles:
                return {'error': 'Unauthorize'}, 401
            else:
                return f(*args, **kwargs)
        return decorated_function
from typing import Sequence
from functools import wraps
from flask import g, abort


def authorized(roles: Sequence[str] = None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if g.user is None or roles is not None and any(role in g.user.roles for role in roles):
                return abort(401, {'error': 'Unauthorize'})
            else:
                return f(*args, **kwargs)
        return decorated_function
    return decorator


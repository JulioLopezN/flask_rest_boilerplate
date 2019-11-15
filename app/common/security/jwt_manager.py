import jwt
from datetime import datetime, timedelta

class JwtManager:
    def __init__(self, secret, algorithm='HS256'):
        self.secret = secret
        self.algorithm = algorithm

    def encode(self, payload: dict, remember_me = False):
        days = 7 if remember_me else 1
        payload['exp'] = datetime.utcnow() + timedelta(days = days)
        
        return jwt.encode(payload, self.secret, self.algorithm)

    def decode(self, token):
        try:
            if token: 
                return jwt.decode(token, self.token, [self.algorithm])
        except:
            return None

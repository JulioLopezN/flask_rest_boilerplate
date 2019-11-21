from typing import Union
import jwt
from datetime import datetime, timedelta


class JwtManager:
    def __init__(self, secret: Union[str, bytes], algorithm='HS256'):
        self.secret = secret
        self.algorithm = algorithm

    def encode(self, payload: dict, remember_me=False):
        days = 7 if remember_me else 1
        payload['exp'] = datetime.utcnow() + timedelta(days=days)

        return jwt.encode(payload, self.secret, self.algorithm)

    def decode(self, token: Union[str, bytes]):
        try:
            return jwt.decode(token, self.secret, [self.algorithm])
        except:
            return None

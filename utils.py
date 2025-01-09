import bcrypt
from typing import Optional

def hash_password(raw_password: str | None):
    assert raw_password, 'Password is required'
    return bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def match_password(raw_password, encoded_password):
    assert raw_password, 'Password is required'
    assert encoded_password, 'Password is required'
    return bcrypt.checkpw(raw_password.encode('utf-8'), encoded_password.encode('utf-8'))


class Response:
    def __init__(self,
                 status_code: int = 200,
                 message: Optional[str] = None):
        self.status_code = status_code
        self.message = message


class BadRequest:
    def __init__(self, status_code: int = 404, message: Optional[str] = None):
        self.status_code = status_code
        self.message = message

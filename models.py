from datetime import datetime
from enum import Enum


class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'


class User:
    def __init__(self,
                 username: str,
                 password: str,
                 user_id: int | None = None,
                 login_try_count: int | None = None,
                 role: UserRole | None = None,
                 created_at: datetime | None = None):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.login_try_count = login_try_count or 0
        self.role = role or UserRole.USER.value
        self.created_at = created_at

    @staticmethod
    def from_tuple(args):
        return User(
            user_id=args[0],
            username=args[1],
            password=args[2],
            login_try_count=args[3],
            role=args[4],
            created_at=args[5]
        )

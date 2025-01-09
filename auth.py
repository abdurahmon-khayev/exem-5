import psycopg2
from dto import UserRegisterDTO
from models import User, UserRole
from session import Session
from utils import BadRequest, match_password, Response, hash_password
from db import cur, commit
from validators import validation_user_on_create

session = Session()

@commit
def login(username: str, password: str):
    user: User | None = session.check_session()
    if user:
        return BadRequest(message="You already logged in.")

    get_user_by_username_query = '''select * from users where username = %s;'''
    data = (username,)
    cur.execute(get_user_by_username_query, data)
    user_data = cur.fetchone()
    if not user_data:
        return BadRequest(message="Username or Password invalid")
    user: User = User.from_tuple(user_data)
    if not match_password(password, user.password):
        user_update_query = '''update users set login_try_count = login_try_count + 1 where username = %s;'''
        data = (user.username,)
        cur.execute(user_update_query, data)
        return BadRequest(message="Username or Password Invalid")
    session.add_session(user)
    return Response(message="Login Successful")


@commit
def register(username: str, password: str):
    try:
        validation_user_on_create(username, password)
        check_user_on_create = '''select * from users where username = %s;'''
        data = (username,)
        cur.execute(check_user_on_create, data)
        user_data = cur.fetchone()
        if user_data:
            return BadRequest(message="User Already Exists")
        user = UserRegisterDTO(username=username, password=password)
        insert_user_query = '''insert into users (username,password,login_try_count,role)
        values (%s,%s,%s,%s);'''
        data = (username, hash_password(password), 0, UserRole.USER.value)
        cur.execute(insert_user_query, data)
        return Response(message="User successfully Registered")
    except AssertionError as e:
        print(e)
    except psycopg2.ProgrammingError as e:
        print(e)


def logout():
    if session.session:
        session.session = None
        return Response(message="Logged Out")

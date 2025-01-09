import psycopg2
import time
from models import UserRole
from utils import Response, hash_password

db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'acorotD7472',
    'database': 'postgres',
    'port': 5432
}

conn = psycopg2.connect(**db_info)
cur = conn.cursor()


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


@commit
def create_table_user():
    query = '''CREATE TABLE IF NOT EXISTS users(
            id serial primary key,
            username varchar(200),
            password text, 
            login_try_count int default 0,
            role varchar(20),
            created_at timestamp default current_timestamp
    );'''

    cur.execute(query)
    return Response(201, 'User Table Created')


def init():
    create_table_user()
    time.sleep(1)


@commit
def migrate():
    query = '''insert into users(username, password, login_try_count, role)
    values (%s, %s, %s, %s);'''
    data = ('admin', hash_password('admin123'), 0, UserRole.ADMIN.value)
    cur.execute(query, data)

import psycopg2



db_info = {
    'host': 'localhost',
    'user': 'postgres',
    'password': '1',
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
def create_table_product():
    query = '''CREATE TABLE IF NOT EXISTS Product(
            id serial primary key,
            name varchar(200),
            price decimal(8,2), 
            color varchar(200), 
            image varchar(255)
    );'''

    cur.execute(query)

if __name__ == '__main__':
    create_table_product()
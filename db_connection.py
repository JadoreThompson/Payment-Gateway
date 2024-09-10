import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool
from contextlib import contextmanager


load_dotenv("../.env")

conn_params = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'dbname': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT')
}

conn_pool = psycopg2.pool.SimpleConnectionPool(minconn=1, maxconn=50, **conn_params)


with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                email VARCHAR(20) UNIQUE NOT NULL,
                fname VARCHAR(20) NOT NULL,
                sname VARCHAR(20) NOT NULL,
                company_name VARCHAR(20),
                password VARCHAR(100) NOT NULL
            );            
        """)
        conn.commit()


@contextmanager
def get_db_conn():
    """
    :yield: DB Connection Object
    """
    conn = conn_pool.getconn()
    try:
        yield conn
    finally:
        conn_pool.putconn(conn)
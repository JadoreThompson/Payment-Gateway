# Directory Modules
from API.models import *
from db_connection import get_db_conn

# FastAPI Modules
from fastapi import APIRouter, HTTPException


auth = APIRouter()


def check_if_user_exists(cur, email):
    cur.execute("""
        SELECT password
        FROM users
        WHERE email = %s;
    """, (email, ))
    return cur.fetchone()


def get_insert_attributes(user: dict) -> tuple:
    """
    :param user:
    :return: Tuple:
        - Column names
        - Placeholder values %s
        - Tuple(values)
    """

    columns = [key for key in user if user[key] != None]
    placeholders = ", ".join(["%s"] * len(columns))
    values = [(user[key], ) for key in user]
    return ", ".join(columns), placeholders, values


@auth.get("/")
async def read_root():
    return {"status": 200, "message": "auth"}


@auth.post("/login")
async def login(user: LoginUser):
    with get_db_conn() as conn:
        with conn.cursor() as cur:
            try:
                # Checking if user exists
                user = check_if_user_exists(cur, user.email)
                if user is None:
                    raise HTTPException(status_code=400, detail="Invalid credentials")

                # TODO: hash pw , begin actual business logic
                return HTTPException(status_code=200, detail="Logged In Successfully")
            except Exception as e:
                conn.rollback()
                print(type(e), str(e))
                raise HTTPException(status_code=500, detail="Something went wrong")


@auth.post("/signup")
async def signup(user: SignUpUser):
    """
    :param user:
    :return: Status Codes
        - 409: User Already Exists
    """

    with get_db_conn() as conn:
        with conn.cursor() as cur:
            try:
                # Checking if user exists
                if check_if_user_exists(cur, user.email):
                    raise HTTPException(status_code=409, detail="User already exists")

                # Insert
                columns, placeholders, values = get_insert_attributes(dict(user))
                cur.execute(f"""
                    INSERT INTO users({columns})
                    VALUES ({placeholders});
                """, values)
                conn.commit()
                return HTTPException(status_code=200, detail="Successfully signed up")
            except Exception as e:
                conn.rollback()
                print(type(e), str(e))
                raise HTTPException(status_code=500, detail="Something went wrong")

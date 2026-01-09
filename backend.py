import pymysql
import re
import bcrypt


def validate_name(name: str) -> bool:
    return bool(re.match(r'^[A-Za-z][A-Za-z0-9]*$', name))


def validate_age(age: int) -> bool:
    return isinstance(age, int) and age > 0


def validate_email(email: str) -> bool:
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email))


def validate_phone(phone: str) -> bool:
    return bool(re.match(r'^\d{10}$', phone))


def validate_password(password: str) -> bool:
    return len(password) >= 6


def user_details(name, age, phoneno, email, password):
    con_obj = None
    cur_obj = None
    try:
        con_obj = pymysql.connect(
            user="root",
            password="root",
            host="localhost",
            database="products"
        )

        cur_obj = con_obj.cursor()

        cur_obj.execute(
            """
            CREATE TABLE IF NOT EXISTS user_info (
                name VARCHAR(20),
                age INT(5),
                phoneno VARCHAR(10),
                email VARCHAR(50),
                password VARCHAR(255)
            );
            """
        )

        # hash password
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        qry = "INSERT INTO user_info (name, age, phoneno, email, password) VALUES (%s, %s, %s, %s, %s)"
        val = (name, age, phoneno, email, hashed)
        cur_obj.execute(qry, val)
        con_obj.commit()

        print("Record inserted successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if cur_obj: cur_obj.close()
        if con_obj: con_obj.close()

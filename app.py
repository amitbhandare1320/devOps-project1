from flask import Flask, render_template, request, redirect, url_for
from backend import (
    user_details,
    validate_name,
    validate_age,
    validate_phone,
    validate_email,
    validate_password
)

import bcrypt
import pymysql

app = Flask(__name__)


# -------------------- WELCOME PAGE --------------------
@app.route("/")
def welcome():
    return render_template("welcome.html")


# -------------------- LOGIN PAGE --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        con = pymysql.connect(
            user="root",
            password="root",
            host="localhost",
            database="products"
        )

        cur = con.cursor()
        cur.execute("SELECT password FROM user_info WHERE email=%s", (email,))
        row = cur.fetchone()

        # check password from DB
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return redirect(url_for("success"))

        return render_template("login.html", error="Invalid email or password")

    return render_template("login.html")


# -------------------- SUCCESS PAGE --------------------
@app.route("/success")
def success():
    return render_template("success.html")


# -------------------- USER FORM PAGE --------------------
@app.route("/index")
def form_page():
    return render_template("index.html", errors={}, values={}, success=None)


# -------------------- SAVE DATA --------------------
@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"].strip()
    age = request.form["age"].strip()
    phone = request.form["phone"].strip()
    email = request.form["email"].strip()
    password = request.form["password"].strip()

    values = dict(name=name, age=age, phone=phone, email=email)
    errors = {}

    if not validate_name(name):
        errors["name"] = "Name must start with a letter and be alphanumeric."

    if not age.isdigit() or not validate_age(int(age)):
        errors["age"] = "Age must be greater than 0."

    if not validate_phone(phone):
        errors["phone"] = "Phone must be 10 digits."

    if not validate_email(email):
        errors["email"] = "Email must be valid."

    if not validate_password(password):
        errors["password"] = "Password must be at least 6 characters."

    if errors:
        return render_template("index.html", errors=errors, values=values)

    # Save to DB
    user_details(name, int(age), phone, email, password)

    # Go to login page after register
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

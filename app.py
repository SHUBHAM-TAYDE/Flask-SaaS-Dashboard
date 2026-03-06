from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# -----------------------------
# Flask Login Setup
# -----------------------------

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# -----------------------------
# User Class
# -----------------------------

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username


# -----------------------------
# Load User from Database
# -----------------------------

@login_manager.user_loader
def load_user(user_id):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username FROM users WHERE id=?",
        (user_id,)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return User(user[0], user[1])

    return None


# -----------------------------
# Login Route
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database/users.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, username FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            login_user(User(user[0], user[1]))
            return redirect(url_for("dashboard"))

    return render_template("login.html")


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


# -----------------------------
# Analytics Page
# -----------------------------

@app.route("/analytics")
@login_required
def analytics():
    return render_template("analytics.html")


# -----------------------------
# Projects Page
# -----------------------------

@app.route("/projects")
@login_required
def projects():
    return render_template("projects.html")


# -----------------------------
# Logout
# -----------------------------

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# -----------------------------
# Run Application
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)

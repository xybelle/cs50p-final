from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = Flask(__name__)

db = SQL("sqlite:///gds.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form.get("fname")
        sname = request.form.get("sname")
        guardian = request.form.get("parent-guardian")
        email = request.form.get("email")
        pw = request.form.get("password")
        conf = request.form.get("confirmation")

        # Check if email is already registered
        stu = db.execute("SELECT email FROM students WHERE email = ?", email)
        existing_stu = stu[0] if stu else None

        # Check if email already exists in the database
        if existing_stu:
            return render_template("apology.html", message="Email already registered. Please try logging in instead.")
        # Validate submission
        elif not fname or not sname:
            return render_template("apology.html", message="Please enter your name")
        # Ensure password is entered
        elif not pw:
            return render_template("apology.html", message="Please enter a password")
        # Ensure password and confirmation matches
        elif pw != conf:
            return render_template("apology.html", message="Passwords do not match")

        # Hash password
        hashed_pw = generate_password_hash(pw, method='pbkdf2', salt_length=2)

        try:
            # Remember students
            db.execute("INSERT INTO students (fname, sname, email, hash, guardian) VALUES (?, ?, ?, ?, ?)",
                       fname, sname, email, hashed_pw, guardian)

        except Exception as e:
            print(e)
            return render_template("apology.html", message="Something went wrong. Please try again.")

        rows = db.execute("SELECT * FROM students WHERE email = ?", email)
        session["user_id"] = rows[0]["id"]

        # Confirm registration
        return redirect("/home")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("email"):
            return render_template("apology.html", message="Please enter your email")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("apology.html", message="Please enter your password")

        # Query database for email
        rows = db.execute(
            "SELECT * FROM students WHERE email = ?", request.form.get("email")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("apology.html", message="Invalid email and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to index
        return redirect("/home")

    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to index
    return redirect("/")


@app.route("/classes")
def classes():
    return render_template("classes.html")


@app.route("/home")
@login_required
def home():
    # Get name to display greeting
    name = db.execute("SELECT guardian FROM students WHERE id = ?", session["user_id"])
    guardian = name[0]

    # Get upcoming classes student already enrolled in
    enrolled = db.execute("SELECT name FROM enrolments WHERE student_id = ?", session["user_id"])
    if enrolled != []:
        enrolled_in = enrolled[0]
        return render_template("home.html", name = guardian, c=enrolled_in)

    return render_template("home.html", name=guardian, c=enrolled)


@app.route("/book", methods=["GET", "POST"])
@login_required
def book():
    if request.method == "POST":
        selected_class = request.form.get('classes')
        return render_template("confirm.html", class_name=selected_class)
    return render_template("book.html")


@app.route("/confirm", methods=["GET", "POST"])
@login_required
def confirm():
    if request.method == "POST":
        selected_class = request.form.get('confirmation')

        # Check if user already enrolled in class
        already_enrolled = db.execute("SELECT name FROM enrolments WHERE name = ? AND student_id = ?", selected_class, session["user_id"])

        if already_enrolled != []:
            return render_template("apology.html", message="You've already enrolled in this class")

        # Update enrolments database
        try:
            class_id = db.execute("SELECT id FROM classes WHERE name = ?", selected_class)
            print(class_id)
            db.execute("INSERT INTO enrolments (class_id, student_id, name) VALUES (?, ?, ?)",
                       class_id[0]['id'], session["user_id"], selected_class)

        except Exception as e:
            print(e)
            return render_template("apology.html", message="Something went wrong. Please try again.")
    return render_template("booked.html")


@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "GET":
        return render_template("change_password.html")

    if request.method == "POST":
        pw = request.form.get("password")
        confirm = request.form.get("confirmation")
        newpw = request.form.get("new_password")

        if not pw or not confirm or not newpw:
            return render_template("apology.html", message="Please enter password")

        # Query database for username
        rows = db.execute("SELECT * FROM students WHERE id = ?", session["user_id"])

        # Check database if old password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], pw):
            return render_template("apology.html", message="Password incorrect")

        if pw != confirm:
            return render_template("apology.html", message="Old password and confirmation don't match")
        else:
            # Hash new password
            hashed_new_pw = generate_password_hash(newpw, method='pbkdf2', salt_length=2)

            # Update database with new hashed password
            db.execute("UPDATE students SET hash = ? WHERE id = ?", hashed_new_pw, session["user_id"])

            return redirect("/")

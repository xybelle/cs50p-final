import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # List of stocks user owns
    stocks = db.execute(
        "SELECT DISTINCT stock FROM transactions WHERE user_id = ? and shares != '0'", session["user_id"])

    # Get user's cash balance
    balance = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    cash_bal = balance[0]['cash']

    portfolio = []

    grand_total = 0
    total_value = 0

    # Get current price of each stock and calculate total value
    for i in range(len(stocks)):
        stock_info = {}
        total_value_ps = 0
        symbol = stocks[i]['stock']
        price = lookup(symbol)
        current_price = price['price']

        # Get number of shares bought
        bought = db.execute(
            "SELECT SUM(shares) FROM transactions WHERE user_id = ? AND stock = ? AND type = 'buy'",
            session["user_id"], stocks[i]['stock'])

        # Get number of shares sold
        sold = db.execute(
            "SELECT SUM(shares) FROM transactions WHERE user_id = ? AND stock = ? AND type = 'sell'",
            session["user_id"], stocks[i]['stock'])

        b = bought[0]['SUM(shares)'] if bought[0]['SUM(shares)'] is not None else 0
        s = sold[0]['SUM(shares)'] if sold[0]['SUM(shares)'] is not None else 0

        # Get shares owned
        shares_owned = b - s

        # Total value of each holding
        total_value_ps = int(current_price) * shares_owned
        total_value += total_value_ps

        # Update stock_info dictionary
        stock_info['symbol'] = symbol
        stock_info['shares'] = shares_owned
        stock_info['xprice'] = current_price
        stock_info['total'] = total_value_ps

        portfolio.append(stock_info)

    # Calculate grand total (stocks total value plus cash balance)
    grand_total = cash_bal + total_value

    return render_template("index.html", stocks=portfolio, balance=cash_bal, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # When requested via GET
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock = lookup(symbol)
        shares = request.form.get("shares")

        if stock == None:
            return apology("Symbol does not exist")
        elif not shares.isdigit():
            return apology("Enter an integer")
        elif shares is None or shares == "" or int(shares) <= 0:
            return apology("Enter the number of shares you wish to buy", 400)
        else:
            rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

            cash_balance = "{:.2f}".format(float(rows[0]["cash"]))
            stock_price = "{:.2f}".format(float(stock["price"]))
            num_shares = "{:.2f}".format(int(shares))
            buy_price = stock_price * num_shares
            balance = "{:.2f}".format(cash_balance - buy_price)

            if balance < 0:
                return apology("Not enough cash balance")
            else:
                id = rows[0]["id"]

                try:
                    # Add transaction to database
                    db.execute("INSERT INTO transactions (type, user_id, stock, shares) VALUES (?, ?, ?, ?)",
                               'buy', id, stock['symbol'], int(shares))

                    # Update cash balance
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", balance, id)
                except Exception as e:
                    print(f"Error inserting/updating transaction/cash balance: {e}")
                    return apology("Error buying shares")

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        history = db.execute("SELECT type, stock, shares, purchase_date FROM transactions WHERE user_id = ?", session["user_id"])
        return render_template("history.html", history=history)

    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # When requested via GET
    if request.method == "GET":
        return render_template("quote.html")

    # When form is submitted via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Enter a stock symbol")

        try:
            stock = lookup(symbol)
        except Exception as e:
            return apology(f"Error looking up stock: {e}")

        # If lookup is unsuccessful
        if stock is None or 'symbol' not in stock:
            return apology("Symbol does not exist")

        price = float(stock['price'])
        stock_price = "{:.2f}".format(price)

        return render_template("quoted.html", price=stock_price, symbol=stock['symbol'])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # When form is submitted via POST
    if request.method == "POST":
        name = request.form.get("username")
        pw = request.form.get("password")
        conf = request.form.get("confirmation")
        user = db.execute("SELECT username FROM users WHERE username = ?", name)
        existing_user = user[0] if user else None

        # Check if user already exists in the database
        if existing_user:
            return apology("Username already exists")
        # Ensure username is entered
        if not name:
            return apology("Please enter a username")
        # Ensure password is entered
        elif not pw:
            return apology("Please enter a password")
        # Ensure password and confirmation matches
        elif pw != conf:
            return apology("Passwords do not match")

        # Hash the password
        hashed_pw = generate_password_hash(pw, method='pbkdf2', salt_length=len(pw))

        # Add user to database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hashed_pw)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        session["user_id"] = rows[0]["id"]
        return redirect("/")

    # When requested via GET
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        options = db.execute(
            "SELECT DISTINCT stock FROM transactions WHERE user_id = ?", session["user_id"])
        return render_template("sell.html", options=options)

    if request.method == "POST":
        print(request.form)
        stock = request.form.get("stock_options")
        shares = request.form.get("shares")
        print(stock)

        # Get number of shares bought
        bought = db.execute(
            "SELECT SUM(shares) FROM transactions WHERE user_id = ? AND stock = ? AND type = 'buy'",
            session["user_id"], stock)
        print(bought)

        # Get number of shares sold
        sold = db.execute(
            "SELECT SUM(shares) FROM transactions WHERE user_id = ? AND stock = ? AND type = 'sell'",
            session["user_id"], stock)
        print(sold)

        b = bought[0]['SUM(shares)'] if bought[0]['SUM(shares)'] is not None else 0
        s = sold[0]['SUM(shares)'] if sold[0]['SUM(shares)'] is not None else 0

        # Get shares owned
        shares_owned = b - s

        if not stock and not shares:
            return apology("Must select stock and enter shares")
        elif int(shares) > shares_owned:
            return apology("You do not have enough shares to sell")
        elif int(shares) <= 0:
            return apology("Enter number of shares you wish to sell")

        updated_shares = shares_owned - int(shares)

        # Add sell transaction to database and handling error
        try:
            db.execute(
                "INSERT INTO transactions (type, user_id, stock, shares) VALUES (?, ?, ?, ?)",
                'sell', session["user_id"], stock, int(shares))
        except Exception as e:
            print(f"Error inserting sell transaction: {e}")
            return apology("Error selling shares")

        # Get current stock price
        xprice = lookup(stock)
        sell_price = xprice['price'] * int(shares)

        # Update cash balance
        db.execute("UPDATE users SET cash = ? WHERE id = ?", sell_price, session["user_id"])

        return redirect("/")


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Change password for user"""

    if request.method == "GET":
        return render_template("change_password.html")

    if request.method == "POST":
        pw = request.form.get("password")
        confirm = request.form.get("confirmation")
        newpw = request.form.get("new_password")

        if not pw or not confirm or not newpw:
            return apology("Please enter password")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )

        # Check database if old password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], pw):
            return apology("Password incorrect")

        if pw != confirm:
            return apology("Old password and confirmation don't match")
        else:
            # Hash new password
            hashed_new_pw = generate_password_hash(newpw, method='pbkdf2', salt_length=len(newpw))

            # Update database with new hashed password
            db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_new_pw, session["user_id"])

            return redirect("/")

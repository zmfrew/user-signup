from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if " " in username or 2 > len(username) or len(username) > 20:
        username_error = "That's not a valid username"

    if " " in password or 2 > len(password) or len(password) > 20:
        password_error = "That's not a valid password"

    if not password == verify_password or verify_password == "":
        verify_password_error = "Passwords don't match"

# TODO: fix this function so that it returns no error for the true emails    
    if not email == "":
        if not "@" in email or "." in email or 2 < len(email) or len(email) < 20:
            email_error = "That's not a valid email"

    return render_template('base.html', username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, verify_password=verify_password, email=email)

@app.route("/")
def index():
    return render_template('base.html')

app.run()
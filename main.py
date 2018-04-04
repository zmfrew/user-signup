from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      

def error_check(text):
    if " " in text or 2 > len(text) or len(text) > 20:
        return True
    else:
        return False

def password_check(pass1, pass2):
    if not pass1 == pass2 or pass2 == "":
        return True
    else:
        return False

def verify_email(email):
    if not "@" in email or not "." in email or 2 > len(email) > 20:
        return True
    else:
        return False

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

    if error_check(username):
        username_error = "That's not a valid username"

    if error_check(password):
        password_error = "That's not a valid password"

    if password_check(password, verify_password):
        verify_password_error = "Passwords don't match"

    if not email == "" and verify_email(email):
        email_error = "That's not a valid email"

    if error_check(username) == False and error_check(password) == False and password_check(password, verify_password) == False:
       return render_template('welcome.html', username=username)

    return render_template('base.html', username_error=username_error, password_error=password_error, 
        verify_password_error=verify_password_error, email_error=email_error, username=username, 
        password=password, verify_password=verify_password, email=email)

@app.route("/")
def index():
    return render_template('base.html')

app.run()
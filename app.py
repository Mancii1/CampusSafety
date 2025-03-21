from flask import Flask, config, render_template, request, redirect, make_response, url_for,session
from werkzeug.security import generate_password_hash , check_password_hash # Import for password hashing
from flask_login import LoginManager,UserMixin, login_user, logout_user
from forms import RegistrationForm, IncidentReportForm  # Import forms
from models import Incident, User, db
from flask_sqlalchemy import SQLAlchemy

import hashlib
import datetime

# Initialize the app
app = Flask(__name__)
app.config.from_object('config.config')


# Initialize the database
db.init_app(app)

# LoginManager is needed for our application 
# to be able to log in and out users
login_manager = LoginManager()
login_manager.init_app(app)



# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/home')
def home():
    if "username" in session:
        return redirect(url_for('report'))
    return render_template('home.html')


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
  # If the user made a POST request, create a new user
    if request.method == "POST":
        user = User(username=request.form.get("username"),
                     password=request.form.get("password"))
        # Add the user to the database
        db.session.add(user)
        # Commit the changes made
        db.session.commit()
        # Once user account created, redirect them
        # to login route (created later on)
        return redirect(url_for("login"))
    # Renders sign_up template if user made a GET request
    return render_template("register.html")



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/resource')
def resource():
    return render_template('resource.html')

@app.route('/about')
def about():
    return render_template('about.html')

with app.app_context():
    db.create_all()  # Create database tables

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

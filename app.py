from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash  # Import for password hashing
from forms import RegistrationForm  # Import the RegistrationForm
from werkzeug.security import generate_password_hash  # Import for password hashing
from config import config
from forms import IncidentReportForm 
from forms import RegistrationForm
from models import Incident, User, db

# Initialize the app
app = Flask(__name__)
app.config.from_object(config)

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple credential check (for demonstration purposes)
        if username == 'admin' and password == 'password':
            return redirect('home.html')
        else:
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password)  # Hash the password
        new_user = User(username=username, password=hashed_password)  # Create a new user instance
        db.session.add(new_user)  # Add the new user to the session
        db.session.commit()  # Commit the session to save the user to the database

        return redirect('login.html')  # Redirect to login after successful registration
    return render_template('register.html', form=form)


@app.route('/dashboard')
def dashboard():
    incidents = Incident.query.all()  # Fetch all incidents from the database
    return render_template('dashboard.html', incidents=incidents)  # Pass incidents to the template


@app.route('/admindashboard')
def admin_dashboard():
    return render_template('admindashboard.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = IncidentReportForm()
    if form.validate_on_submit():
        incident_type = form.incident_type.data
        incident_description = form.incident_description.data
        new_incident = Incident(incident_type=incident_type, incident_description=incident_description)  # Create a new incident instance
        db.session.add(new_incident)  # Add the new incident to the session
        db.session.commit()  # Commit the session to save the incident to the database
        return redirect('/dashboard')  # Redirect to dashboard after successful report
    return render_template('report.html', form=form)


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

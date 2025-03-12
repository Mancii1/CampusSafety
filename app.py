from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def home():
    return render_template('dashboard.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True) 
    password = db.Column(db.String(128))

    incidents = db.relationship('Incident', backref='user', lazy=True)
    # Removed user_id as it is not utilized

    def __repr__(self):
        return f"User('{self.username}')"

class Incident(db.Model):
    __tablename__ = 'incidents'
    id = db.Column(db.Integer, primary_key=True)
    incident_id = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    incident_type = db.Column(db.String(20))
    incident_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    incident_location = db.Column(db.String(20))
    incident_description = db.Column(db.String(200))

    def __repr__(self):
        return f"Incident('{self.incident_type}','{self.incident_description}')"

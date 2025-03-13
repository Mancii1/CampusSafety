from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(20), nullable=False)
    Email = db.Column(db.String(20), unique=True, nullable=False)
    PasswordHash = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"User('{self.Username}', '{self.Email}')"
    
class Incident(db.Model):
    IncidentID = db.Column(db.integer, primary_key=True)
    UserID = db.Column(db.integer, db.ForeignKey('user.UserID'))
    IncidentType = db.Column(db.String(10), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Location = db.Column(db.String(20), nullable=False)
    DateTime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    User = db.relationship('User', backref=db.backref('incidents', Theft=True))

    def __repr__(self):
        return f"Incident('{self.IncidentType}', '{self.Description}')"
    
class SafetyResource(db.Model): 
    ResourceID = db.Column(db.Integer, primary_key=True) 
    ResourceType = db.Column(db.String(25), nullable=False) 
    ResourceName = db.Column(db.String(50), nullable=False) 
    ResourceDescription = db.Column(db.Text) 
    ResourceContact = db.Column(db.String(10))

    def __repr__(self): 
      return f"SafetyResource('{self.ResourceType}', '{self.ResourceName}')"
     
class SafetyTip(db.Model): 
    TipID = db.Column(db.Integer, primary_key=True) 
    TipTitle = db.Column(db.String(50), nullable=False) 
    TipDescription = db.Column(db.Text, nullable=False)

    def __repr__(self): 
     return f"SafetyTip('{self.TipTitle}', '{self.TipDescription}')" 

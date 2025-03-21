from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    submit = SubmitField('Register')

class IncidentReportForm(FlaskForm):
    incident_type = StringField('Incident Type', validators=[DataRequired(), Length(max=50)])
    incident_description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Report Incident')

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from app.models import Service

class BookingForm(FlaskForm):
    patient_name = StringField('Patient Name', validators=[DataRequired(), Length(max=100)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = TextAreaField('Address', validators=[DataRequired()])
    service = SelectField('Service', coerce=int, validators=[DataRequired()])
    preferred_date = DateTimeField('Preferred Date/Time', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Book Now')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service.choices = [(s.id, s.name) for s in Service.query.all()]

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
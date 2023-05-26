from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TimeField, URLField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class NewCafe(FlaskForm):
    # Basics
    name = StringField('Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    map_url = URLField('Map Url')
    img_url = URLField('Image')

    # Space
    restroom = StringField('Is there a restroom?', validators=[DataRequired()])

    seats = StringField('Number of Seats', validators=[DataRequired()])

    # Time
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])

    # Productivity
    wifi = SelectField('Is there Wi-Fi',
                       validators=[DataRequired()],
                       choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    sockets = SelectField('Is it easy to find power sockets?',
                          validators=[DataRequired()],
                          choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])

    # Services
    coffee = SelectField('Is coffee available?',
                         validators=[DataRequired()],
                         choices=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    coffee_price = StringField('Coffee Price?',
                               validators=[DataRequired()])

    # Submit
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')



from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    # import required validators and send the parameters that you require
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2, max=20)]) # type of string + validations
    email = StringField("Email", 
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()]) # we can add additional validators too
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")]) # confirm password should be equal to the entered password
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    # import required validators and send the parameters that you require
    email = StringField("Email", 
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()]) # we can add additional validators too
    remember = BooleanField("Remember Me") # for checking to remember using secure cookies
    submit = SubmitField("Login")

# secret key will protect from modifying cookies etc.
    
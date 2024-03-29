from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed ## for image uploading
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    # import required validators and send the parameters that you require
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2, max=20)]) # type of string + validations
    email = StringField("Email", 
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()]) # we can add additional validators too
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")]) # confirm password should be equal to the entered password
    submit = SubmitField("Sign Up")
    
    # validation before commiting to db
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username is taken. Please choose a different one")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is taken. Please choose a different one")

class LoginForm(FlaskForm):
    # import required validators and send the parameters that you require
    email = StringField("Email", 
                        validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()]) # we can add additional validators too
    remember = BooleanField("Remember Me") # for checking to remember using secure cookies
    submit = SubmitField("Login")

# secret key will protect from modifying cookies etc.


## Account Form
class UpdateAccountForm(FlaskForm):
    # import required validators and send the parameters that you require
    username = StringField("Username", 
                           validators=[DataRequired(), Length(min=2, max=20)]) # type of string + validations
    email = StringField("Email", 
                        validators=[DataRequired(), Email()])
    
    picture = FileField("Update profile picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("Confirm Changes")
    
    # this is now for updation, raise error only if the user changes his/her username or pass. else continue
    # since you should check this for the logged in user, we import current_user from flask_login
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("Username is taken. Please choose a different one")
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("Email is taken. Please choose a different one")




class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")

    
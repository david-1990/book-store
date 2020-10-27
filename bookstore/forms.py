from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'png', 'jpg', 'JPG', 'PNG'}


class ItemForm(FlaskForm):
    name = StringField('Title', validators=[InputRequired()])
    author = StringField('Author', validators=[InputRequired()])
    isbn = StringField('ISBN', validators=[InputRequired()])
    category = StringField('Title', validators=[InputRequired()])
    name = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Product Image', validators=[FileRequired(message='Image can not be empty'),
                                                       FileAllowed(ALLOWED_FILE, message='Only support png, jpg, JPG, PNG, bmp')])
    currency = StringField('Starting Bid', validators=[InputRequired()])
    listing_status = StringField('Availability', validators=[InputRequired()])

    submit = SubmitField("List a Book")

    # this should already be there in the forms.py


class ReviewForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Submit')


# creates the login information
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[
                           InputRequired('Enter username')])
    password = PasswordField("Password", validators=[
                             InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[
                           Email("Please enter a valid email")])

    # linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                                                     EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    # submit button
    submit = SubmitField("Register")

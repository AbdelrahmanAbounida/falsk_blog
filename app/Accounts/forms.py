from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,IntegerField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.extensions import mongo_db

class RegisterForm(FlaskForm):
    username = StringField('Username')
    phoneNumber = IntegerField('phone')
    email = EmailField('Email',validators=[DataRequired(),Email("Please enter a correct email address")])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,message="Password length shouldn't be less than 4")])
    confirm_password = PasswordField('Confirm password',validators=[DataRequired(),EqualTo("password")])

    # def validate_email(self,email):
    #     user = mongo_db.blog_collection.find({ "email": email})
    #     if user:
    #         raise ValidationError("Opss!! a user with same email already exists.") 


class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email("Please enter a correct email address")])
    password = PasswordField('password',validators=[DataRequired()])


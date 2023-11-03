from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, TextAreaField, IntegerField
from wtforms.validators import DataRequired,Length



class RegisterForm(FlaskForm):
    '''Register Form'''
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    cpassword = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class AddProductForm(FlaskForm):
    '''AddProductForm'''
    productname = StringField('Product Name', validators=[DataRequired(), Length(1, 64)])
    description = TextAreaField('Product Description', validators=[DataRequired(), Length(1, 64)])
    stock = IntegerField('Stock Available', validators=[DataRequired()])
    ssubmit = SubmitField('Add product')
    
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask import current_app

## Validators 

def AllowedFileValidator(form,field):
    if not ('.' in field.data.filename and 
        field.data.filename.rsplit('.', 1)[1].lower() in current_app.config['BACKGROUND_ALLOWED_EXTENSIONS']):
        raise ValidationError(f"Allowd file types are: [ {', '.join(current_app.config['BACKGROUND_ALLOWED_EXTENSIONS'])} ] only")
    


# (value,displayedOption)
blog_categories = [(None,'Choose Category'),('Food','Food'),('Travel','Travel'),('Lifestyle','Lifestyle'),('Science','Science')]

class PostForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    background = FileField('background',validators=[DataRequired(),AllowedFileValidator])
    category = SelectField('category',choices=blog_categories,validators=[DataRequired()])
     
    
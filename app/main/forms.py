from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired

# (value,displayedOption)
blog_categories = [('Food','Food'),('Travel','Travel'),('Lifestyle','Lifestyle'),('Science','Science')]

class PostForm(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    background = FileField('background',validators=[DataRequired()])
    category = SelectField('category',choices=blog_categories,validators=[DataRequired()])
     

from . import main 
from flask import render_template,request, flash
from app.extensions import mongo_db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    # mongo_db['blog_collection'].insert_one({'name':'Abdelrahman'})
    flash('user has been added successfully','success')
    return render_template('about.html')

@main.route('/game')
def game():
    return render_template('game.html')


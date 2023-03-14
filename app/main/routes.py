from . import main 
from flask import render_template,redirect, flash
from app.extensions import mongo_db
from .forms import RegisterForm


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


@main.route('/all_posts')
def allPosts():
    return render_template('allPosts.html')

@main.route('/my_posts')
def myPosts():
    return render_template('myPosts.html')

@main.route('/all_videos')
def allVideos():
    return render_template('allVideos.html')

@main.route('/my_videos')
def myVideos():
    return render_template('myVideos.html')
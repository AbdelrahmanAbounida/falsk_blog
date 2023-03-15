from . import main 
from flask import render_template,redirect, flash,request,current_app, send_from_directory
from app.extensions import mongo_db
from .forms import PostForm
from flask_login import login_required
import os 
from werkzeug.utils import secure_filename
from pathlib import Path

@main.route('/',methods=['GET','POST'])
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
@login_required
def myPosts():
    posts = []
    if not len(posts):
        flash("You don't have any posts yet","warning")
    return render_template('myPosts.html',posts=posts)

@main.route('/all_videos')
def allVideos():
    return render_template('allVideos.html')


@main.route('/my_videos')
@login_required
def myVideos():
    return render_template('myVideos.html')


########################
# File Handling
########################

@main.route('/create_post',methods=['GET','POST'])
@login_required
def addPost():
    form = PostForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            file = form.background.data
            filename = file.filename
            if file :
                file_name = secure_filename(file.filename)
                file.save(os.path.join(Path(__file__).resolve().parent.parent,current_app.config['UPLOAD_FOLDER'],file.filename))
            else:
                print("There is no file")
        else:
            print("Form not valid")

    return render_template('addPost.html',form=form)



@main.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(Path(__file__).resolve().parent.parent,current_app.config['UPLOAD_FOLDER']), filename)
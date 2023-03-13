from flask import render_template, redirect, request,flash
from .forms import RegisterForm, LoginForm
from . import accounts
from app.extensions import mongo_db,custom_bcrypt, login_manager
from flask_login import current_user, login_required, login_user

@login_manager.user_loader
def load_user(user_id):
    return mongo_db.find_one({'id':user_id})

@accounts.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # retrieve form data
            username = form.username.data
            phone = form.phoneNumber.data
            email = form.email.data
            password = custom_bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            # add to database
            mongo_db['blog_collection'].insert_one({'username':username,'phone':phone,'email':email,'password':password})
            flash(f'Account Created for {form.username.data}','success')
            return redirect('/')
        else:
            print("no")
    return render_template('auth/register.html',form=form)


@accounts.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')

    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = mongo_db['blog_collection'].find_one({'emial':form.email.data})

            if user and custom_bcrypt.check_password_hash(user['password'],form.password.data):
                login_user(user)
                return redirect('/')
            else:
                flash('Login unsuccessful. Please check your email or password', 'warning')
        else:
            print("Noo")
    return render_template('auth/login.html',form=form)


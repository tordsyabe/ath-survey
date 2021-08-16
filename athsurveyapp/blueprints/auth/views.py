from flask import Blueprint, render_template, redirect, url_for, request, flash
from athsurveyapp.models.models import User, db
from athsurveyapp.blueprints.auth.forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth_page = Blueprint('auth_page', __name__, template_folder="templates")

@auth_page.route('/user')
@login_required
def users_index():
    
    users = User.query.all()
    
    return render_template('users.html', users=users)

@auth_page.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        
        email = form.email.data
        password = form.password.data
        remember = True if form.remember.data else False

        user = User.query.filter_by(email=email).first()
        
        print(user)

        if not user:
            flash('Please check your login details and try again', 'danger')
            return redirect(url_for('auth_page.login'))
        
        if not check_password_hash(user.password, password):
            flash('Please check your login details and try again', 'danger')
            return redirect(url_for('auth_page.login'))
        
        login_user(user, remember=remember)
        
        return redirect(url_for('dashboard.dashboard'))

    return render_template('login.html', form=form)

@auth_page.route('/register', methods=['GET', 'POST'])
@login_required
def create_user():
    
    form = RegisterForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.name.data
        user_email = form.email.data
        user_password = form.password.data
        user_is_admin = True if form.is_admin.data else False
        
        user = User.query.filter_by(email=user_email).first()
        
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth_page.create_user'))
        
        hashed_password = generate_password_hash(user_password, method='sha256')
        print(len(hashed_password))

        new_user = User(user_email, hashed_password, user_name, user_is_admin)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth_page.users'))
    
    return render_template('register.html', form=form)

@auth_page.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', "success")
    return redirect(url_for('auth_page.login'))
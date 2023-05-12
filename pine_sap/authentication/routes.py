from flask import Blueprint, render_template, request, redirect, url_for, flash
from pine_sap.forms import UserLoginForm
from pine_sap.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods = ['GET','POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            print(email, username, password)

            user = User(email, username, password=password)

            db.session.add(user)
            db.session.commit()

            flash(f"You have created a user acount {username}, user-created")

            return redirect(url_for('auth.signin'))
        
    except:
        raise Exception('Invalid Form Data: Please change your form')

    return render_template('signup.html', form=form)


@auth.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)
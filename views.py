from flask import render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm
from models import User
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db
from mail import send_mail
from models import ConfirmResult

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # la funzione flash ci permette di mandare dei banner a video
        flash("Account successfully created!")
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        # Prende due parametri: l'utente e il secondo parametro indica se l'utente deve rimanere loggato o meno
        # login_user(user, False)
        # return redirect(url_for("index"))

        # Invece di loggare l'utente (come sopra) invio l'email di conferma
        send_mail(user.email, "Confirm your email", "mails/email_confirm", user=user, token=user.generate_confirmation_token())

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):

            if not user.confirmed:
                flash("Check your inbox to confirm your account.")
            else:
                login_user(user, form.remember_me.data)
                return redirect(url_for('index'))
        else:
            flash("Invalid email or password")

    return render_template('login.html', form=form)


# il decoratore @login_required inibisce delle route se l'utente non è loggato
# rimandandolo alla view specificata all'interno del campo login_manager.login_view = "login" presente sotto app.py
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for('index'))

@app.route('/')
@login_required
def index():
    # l'utilizzo del passaggio del current_user è superfluo, inquanto è accessibile da tutte le view e da tutti i file Python
    return render_template('index.html', user=current_user)

@app.route('/confirm/<token>')
def confirm(token):

    result = User.confirm(token)

    if result == ConfirmResult.CONFIRMED:
        flash("You have confirmed your account. You can login now!")
    elif result == ConfirmResult.ALREADY_CONFIRMED:
        flash("You have already confirmed your account.")
    else:
        flash("The confirmation link is invalid!")

    return redirect(url_for("login"))



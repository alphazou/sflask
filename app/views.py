from app import app
from flask import request, render_template, jsonify, \
    flash, url_for, current_app, g, redirect, session
import time, datetime
from .forms import LoginForm



@app.route('/')
def index():
    if session.get('user'):
        flash('{}，你已登录'.format(session['user']))
        return render_template('index.html',
                               current_time = datetime.datetime.utcnow(),
                               user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    email = None
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'nx_xiaozi@163.com' \
            and form.password.data == 'b091880':
            session['user'] = form.email.data
            return redirect(url_for('index'))
    return render_template('login.html',
                           form=form)

@app.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('login'))






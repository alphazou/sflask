from app import app, mail
from flask import request, render_template, jsonify, \
    flash, url_for, current_app, g, redirect, session
import time, datetime
from .forms import LoginForm
from .models import *
from flask_mail import Message
from threading import Thread

#首页
@app.route('/')
def index():
    if session.get('user'):
        # flash('{}，你已登录'.format(session['user']))
        # send_email('nx_xiaozi@qq.com',
        #            '通知：用户登录',
        #            'mail/new_user',
        #            user = session['user'])
        return render_template('index.html',
                               current_time = datetime.datetime.utcnow(),
                               user=session['user'])
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name_email = form.name_or_email.data
        passwd = form.password.data
        if '@' in name_email:
            user = User.query.filter_by(email=name_email).first()
        else:
            user = User.query.filter_by(username=name_email).first()
        if user:
            if user.password == passwd:
                session['user'] = user.username
                flash('欢迎你，{}！'.format(user.nickname))
                return redirect(url_for('index'))
            else:
                flash('密码错误')
        else:
            flash('用户名或邮箱不存在！')

    return render_template('login.html',
                           form=form)

@app.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('login'))


# 发邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJIECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr




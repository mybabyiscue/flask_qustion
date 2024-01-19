# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: user.py
@time: 2022/4/24 16:27
"""
from datetime import datetime

from flask import Blueprint, render_template, request, redirect, \
    url_for, jsonify, session,flash
from werkzeug.security import generate_password_hash, check_password_hash
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchModel, Usermodel
import string
import random
from .forms import RegisterForm, LoginForm

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = Usermodel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect('/')
            else:
                flash("邮箱或密码错误")
                return redirect(url_for('user.login'))
        else:
            flash("邮箱或密码格式错误")
            return redirect(url_for('user.login'))  # 返回登录页面


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # md5加密
            hash_password = generate_password_hash(password)
            user = Usermodel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return render_template('register.html', form=form)


@bp.route("/captcha", methods=['POST'])
def get_captcha():
    """
    获取验证码
    :return:
    """
    #  使用get post方法
    email = request.form.get('email')
    # 随机生成一个字符串
    s = string.ascii_letters + string.digits
    captcha = "".join(random.sample(s, 4))
    if email:
        message = Message("测试邮件", recipients=[email], body=f"【谢军问答】，您的验证码是：{captcha}")
        mail.send(message)
        captcha_model = EmailCaptchModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print("captcha:", captcha)
        return jsonify({"code": 200, "msg": "获取成功"})
    else:
        return jsonify({"code": 400, "msg": "请先传递邮箱！"})

@bp.route('/logout')
def logout():
    # 清楚session所有数据
    session.clear()
    return redirect(url_for('user.login'))  #
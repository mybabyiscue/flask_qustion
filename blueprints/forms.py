# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: forms.py
@time: 2022/4/25 17:23
"""
import wtforms
from wtforms.validators import length, email, EqualTo, InputRequired
from models import EmailCaptchModel, Usermodel


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(
        label='用户名',
        validators=[wtforms.validators.DataRequired(message='用户名不能为空'),
                    length(min=3, max=20, message='用户名长度必须在3-20之间')],
        description='用户名',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '请输入用户名',
        }

    )
    password = wtforms.PasswordField(
        label='密码',
        validators=[wtforms.validators.DataRequired(message='密码不能为空'),
                    length(min=6, max=20, message='密码长度必须在6-20之间')],
        description='密码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '请输入密码',
        }

    )
    password_confirm = wtforms.PasswordField(
        label='确认密码',
        validators=[wtforms.validators.DataRequired(message='密码不能为空'), EqualTo('password', message='两次密码不一致')],
        description='密码',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '请输入密码',
        })

    email = wtforms.StringField(
        label='邮箱',
        validators=[wtforms.validators.DataRequired(message='邮箱不能为空'), wtforms.validators.Email(message='邮箱格式不正确')],
        description='邮箱',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '请输入邮箱',
        }
    )
    captcha = wtforms.StringField(
        label='邮箱',
        validators=[wtforms.validators.DataRequired(message='验证码不能为空'),
                    length(min=4, max=4)],
        description='邮箱',
        render_kw={
            'class': 'form-control input-lg',
            'placeholder': '请输入邮箱',
        }
    )

    # phone = wtforms.StringField(
    #     label='手机',
    #     validators=[wtforms.validators.DataRequired(message='手机不能为空'), wtforms.validators.Regexp('1[3458]\\d{9}', message='手机格式不正确')],
    #     description='手机',
    #     render_kw={
    #         'class': 'form-control input-lg',
    #         'placeholder': '请输入手机',
    #     }
    def validate_captcha(self, field):
        email = field.data
        user_model = Usermodel.query.filter_by(email=email).first()
        if user_model:
            raise wtforms.ValidationError('邮箱已经存在')


class LoginForm(wtforms.Form):
    email = wtforms.StringField(
        validators=[wtforms.validators.DataRequired(message='邮箱不能为空'), wtforms.validators.Email(message='邮箱格式不正确')])
    password = wtforms.PasswordField(
        validators=[wtforms.validators.DataRequired(message='密码不能为空'), length(min=6, max=20, message='密码长度必须在6-20之间')])


class QusetionForm(wtforms.Form):
    title = wtforms.StringField(
        validators=[wtforms.validators.DataRequired(message='标题不能为空'), length(min=2, max=60, message='标题长度必须在2-20之间')])
    content = wtforms.TextAreaField(
        validators=[wtforms.validators.DataRequired(message='内容不能为空'),
                    length(min=8, max=10000, message='内容长度必须在8-200之间')])


class AnswerForm(wtforms.Form):
    content = wtforms.TextAreaField(
        validators=[wtforms.validators.DataRequired(message='内容不能为空'),
                    length(min=1, message='内容长度必须在超过1个字符')])
    # question_id = wtforms.IntegerField(validators=[InputRequired()])

# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: exts.py
@time: 2022/4/24 16:25
"""
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
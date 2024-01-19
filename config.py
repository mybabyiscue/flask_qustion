# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: config.py
@time: 2022/4/24 16:18
"""
# 数据库配置信息
import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'xt_flask'
USERNAME = 'admin'
PASSWORD = 'cstorfs'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI  # 配置数据库连接
SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = "ssyuyttsjdhajshdjkahsd11232334667"
# print(SECRET_KEY)

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1142279711@qq.com"
MAIL_PASSWORD = "wxhqmmzdnahnbage"
MAIL_DEFAULT_SENDER = "1142279711@qq.com"

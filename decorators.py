# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: decorators.py
@time: 2022/4/27 14:21
"""
from flask import g, redirect, url_for
from functools import wraps


def login_required(func):  # 定义装饰器
    @wraps(func)  # 保留原函数的__name__属性
    def wrapper(*args, **kwargs):  # 参数
        if hasattr(g, 'user'):  # 判断g对象是否有user属性
            return func(*args, **kwargs)  # 如果用户已经登录，则执行视图函数
        else:
            return redirect(url_for('user.login'))

    return wrapper

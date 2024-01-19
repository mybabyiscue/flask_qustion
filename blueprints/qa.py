# encoding: utf-8
"""
@author: xiejun
@contact: 1079658140@qq.com
@software: PyCharm
@file: qa.py
@time: 2022/4/24 16:27
"""

from flask import Blueprint, render_template, request, g, redirect, url_for, flash
from sqlalchemy import or_

from blueprints.forms import QusetionForm, AnswerForm
from decorators import login_required
from exts import db
from models import QuestionModel, AnswerModel

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def index():
    questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template('index.html', questions=questions)


@bp.route('/question/public', methods=['GET', 'POST'])
@login_required  # 装饰器，需要登录才能访问
def public_question():
    # 判断是否登录，如果没有登录，跳转到登录页面
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QusetionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            flash('标题或格式错误')
            return redirect(url_for("qa.public_question"))


@bp.route("/question/<int:question_id>")
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)
    return render_template('detail.html', question=question)


@bp.route("/answer/<int:question_id>", methods=['POST'])
@login_required
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        # question_id = form.question_id.data
        answer_model = AnswerModel(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect(url_for('qa.question_detail', question_id=question_id))
    else:
        flash('回答格式错误')
        return redirect(url_for('qa.question_detail', question_id=question_id))


@bp.route("search")
def search():
    q = request.args.get('q')
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(q),
                                               QuestionModel.content.contains(q))).order_by(db.text("-create_time"))
    return render_template('index.html', questions=questions)

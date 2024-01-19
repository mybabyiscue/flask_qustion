from flask import Flask, session, g
import config
from exts import db, mail
from blueprints import qa_bp
from blueprints import user_bp
from flask_migrate import Migrate
from models import Usermodel

app = Flask(__name__)
app.config.from_object(config)  # 导入配置文件
db.init_app(app)  # 初始化数据库
mail.init_app(app)  # 初始化邮件
# 表结构都放在models.py文件中
migrate = Migrate(app, db)  # 初始化数据库迁移

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def before_request():
    # 在请求前执行
    user_id = session.get('user_id')
    if user_id:
        try:
            user = Usermodel.query.get(user_id)
            # 将user添加到g对象中,他的值是user这个变量
            # setattr(g, 'user', user)
            g.user = user  # 全局变量
        except:
            g.user = None


# 请求来了->before request->视图函数->视图函数中返回模板->context_processor


@app.context_processor  # 上下文模板
def context_processor():
    # 在模板中可以直接调用g.user
    # return {'user': g.user}
    if hasattr(g, 'user'):
        return {'user': g.user}
    else:
        return {}  # 如果没有user,返回空字典


if __name__ == '__main__':
    app.run()

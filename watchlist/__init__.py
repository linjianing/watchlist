from flask import Flask
import os
import sys

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)


login_manager = LoginManager(app)  # 实例化扩展类
login_manager.login_view = 'login'
# login_manager.login_message 定义错误提示信息


# 视图部分
@app.context_processor
def inject_user():  # 函数名任意
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)  # 以字典形式返回


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户ID作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id))  # 用ID作为User模型的主键查询对应的用户
    return user  # 返回用户对象


from watchlist import views, errors, commands  # 防止模块冲突，将这几个模块放在最后导入

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_mail import Mail, Message

# 创建 Flask 应用程序对象
app = Flask(__name__,static_url_path='/static')

# 导入配置
app.config.from_object('config.Config')

# 初始化数据库
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 初始化邮件
mail = Mail(app)

# 导入视图和模型
from app import routes, models

with app.app_context():
    db.create_all()


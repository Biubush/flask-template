from app import db
from datetime import datetime


# 用户表
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"


# 帖子表
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"


# 操作数据库user表的类
class UserOperate:
    # 添加用户
    def add_user(self, username, email, password):
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    # 查询用户
    def query_user(self, username):
        user = User.query.filter_by(username=username).first()
        return user

    # 查询所有用户
    def query_all_user(self):
        users = User.query.all()
        return users

    # 删除用户
    def delete_user(self, username):
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return user

    # 修改用户
    def update_user(self, username, **kwargs):
        user = User.query.filter_by(username=username).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user

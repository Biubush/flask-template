from flask import render_template, request, redirect, url_for
from app import *
from app.models import *

# 首页路由
@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

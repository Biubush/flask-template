from app import app, db
from app.models import *
from faker import Faker

fake = Faker()

# 生成虚拟用户数据
def generate_users(num_users):
    for _ in range(num_users):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        user = User(username=username, email=email, password=password)
        db.session.add(user)
    db.session.commit()

# 生成虚拟帖子数据
def generate_posts(num_posts):
    users = User.query.all()
    for _ in range(num_posts):
        title = fake.sentence()
        content = fake.paragraph()
        user_id = fake.random_element(users).id
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        generate_users(10)
        generate_posts(50)

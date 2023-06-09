from app import app, upgrade, mail, Message
from config import Config


def send_email(title, to_, body, html):
    with app.app_context():
        msg = Message(title, sender=Config.MAIL_USERNAME, recipients=to_)
        msg.body = body
        msg.html = html
        mail.send(msg)
        return "Email sent successfully!"


import subprocess


def check_and_migrate():
    # 执行 flask migrate 命令来检测和应用数据库迁移
    result = subprocess.run(
        ["flask", "db", "upgrade", "--directory", "migrations", "--sql"],
        capture_output=True,
        text=True,
    )
    if "No migrations to apply" in result.stdout:
        print("数据库已是最新版本，无需迁移。")
    elif "Running upgrade" in result.stdout:
        with app.app_context():
            upgrade()
        print("数据库已更新至最新版本！")
    else:
        print("检测和迁移过程中出现错误：")
        print(result.stderr)

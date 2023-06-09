import os,sys

class Config:
    # 应用程序密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YOUR_SECRET_KEY'

    # 数据库配置
    WIN = sys.platform.startswith('win')
    if WIN:
        prefix = 'sqlite:///'
    else:
        prefix = 'sqlite:////'
    base_dir = os.path.abspath(os.path.dirname(__file__))
    if not os.path.exists(f'{base_dir}/.database/data.sqlite'):
        os.mkdir(f'{base_dir}/.database')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'{prefix}{base_dir}/.database/data.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #邮件配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #其他配置
    JSON_AS_ASCII = False

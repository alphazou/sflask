import os


DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'b091880'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:b091880@localhost/sflask?charset=utf8'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER = 'imap.163.com'
MAIL_PORT = 993 # imap993,smtp465或者994
MAIL_USE_TLS = True
MAIL_USERNAME = 'nx_xiaozi'     # os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = 'b091880!'            # os.environ.get('MAIL_PASSWORD')

FLASKY_MAIL_SUBJIECT_PREFIX = '[Flasky]'     # 邮件主题
FLASKY_MAIL_SENDER = 'Flasky Admin <nx_xiaozi@163.com>'  #邮件发送者地址




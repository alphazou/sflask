import os


DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'b091880'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:b091880@localhost/sflask?charset=utf8'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

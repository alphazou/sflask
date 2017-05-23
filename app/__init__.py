from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object('config')
manager = Manager(app)
db = SQLAlchemy(app)
migrage = Migrate(app, db)
manager.add_command('db', MigrateCommand)

from app import views


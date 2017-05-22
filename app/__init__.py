from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object('config')
manager = Manager(app)
db = SQLAlchemy(app)


from app import views


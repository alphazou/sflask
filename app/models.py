from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    # __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), default='000000')
    nickname = db.Column(db.String(48))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# 删除和创建表
db.drop_all()
db.create_all()

# 添加字段
admin_role = Role(name='admin')
user_role = Role(name='user')
db.session.add_all([admin_role, user_role])

user_xiaozi = User(username='xiaozi', nickname='娜西小子', email='nx_xiaozi@163.com',password='b091880', role=admin_role)
db.session.add(user_xiaozi)

for i in range(1,10):
    db.session.add(User(username='user{}'.format(i), role=user_role))

db.session.commit()

#查询
# user8 = User.query.filter_by(username='user8').first()
# role_user = Role.query.filter_by(name='user').first()
# print(role_user.users.order_by(User.username).all())
# print(user8.role)
# print(role_user.users.count())


#删除
# user8 = User.query.filter_by(username='user8').first()
# db.session.delete(user9)
# db.session.commit()
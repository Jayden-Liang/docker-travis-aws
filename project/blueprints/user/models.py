from sqlalchemy import or_
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role', back_populates= 'users')

    blogs = db.relationship('Blog', back_populates= 'user')


    @classmethod
    def encryptpassword(cls, password, salt='$!@>HUI&DWQa`'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2

    @classmethod
    def find_by_identity(cls, identity):
        return User.query.filter(or_(User.username == identity, User.email == identity)).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(64), unique=True)
    content= db.Column(db.String(5000))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates= 'blogs')

    def save(self):
        db.session.add(self)
        db.session.commit()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index= True)
    users = db.relationship('User', back_populates= 'role')

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from datetime import datetime
from flask_login import UserMixin


db = SQLAlchemy(app)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    pwd_hash = db.Column(db.String(200))

    def set_password_hash(self,pwd):
        self.pwd_hash = generate_password_hash(pwd)

    def check_password_hash(self,pwd):
        return check_password_hash(self.pwd_hash, pwd)
    


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    body = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.now)
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))
    tag = db.relationship('Tag', back_populates='posts')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    posts = db.relationship('Post', back_populates='tag')











from . import db
from datetime import datetime
from flask_login import UserMixin



class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))
    isbn = db.Column(db.String(50))
    timeleft = db.Column(db.String(80))

    comments = db.relationship('Comment', backref='item')

    def __repr__(self):
        str = '<Name {0}>'
        str.format(self.name)
        return str

    # def __init__(self, name, description, image_url, currency):
    #    self.name = name
    #    self.description = description
    #    self.image = image_url
    #    self.currency = currency
    #    self.comments = list()
    #Item
    

    # def set_comments(self,comment):
    #    self.comments.append(comment)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

    # def __init__(self,user, text, created_at):
    #    self.user = user
    #    self.text = text
    #    self.created_at = created_at

    # def __repr__(self):
    #    str = 'User {0}, \n Text {1}'
    #    str.format(self.user, self.text)
    #    return str


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    comments = db.relationship('Comment', backref='user')

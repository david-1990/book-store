from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    reviews = db.relationship('Review', backref='user')
    # bids = db.relationship('Bid', backref='user')

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80))
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3), nullable=False)
    listing_status = db.Column(db.String(10))
    timeleft = db.Column(db.String(80))

    bids = db.relationship('Bid', backref='item')
    reviews = db.relationship('Review', backref='item')

    def __repr__(self):
        return '<Name: {}>'.format(self.name)

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    def __repr__(self):
        return '<Review: {}>'.format(self.text)

class Bid(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    highest_bid = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    watchlist = db.relationship('Watchlist', backref='bid')

    def __repr__(self):
        return '<Bid: {}>'.format(self.highest_bid)

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    total_bids = db.Column(db.Integer)
    listing_status = db.Column(db.String(10))

    bid_id = db.Column(db.Integer, db.ForeignKey('bids.id'))

    def __repr__(self):
        return '<Watchlist: {}>'.format(self.name)

from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from .models import Item

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@mainbp.route('/search')
def search():
    #get the string from request
    if request.args['search']:
        dest = "%" + request.args['search'] + '%'
        #use filter and like function to search for matching items
        items = Item.query.filter(Item.name.like(dest)).all()
        #render index.html with few items
        return render_template('index.html', items=items)
    else:
        return redirect(url_for('main.index'))

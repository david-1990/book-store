from flask import Blueprint, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from .models import Item

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

#@mainbp.route('/')
#def index():
#    if 'email' in session:
#        str='<h1>Email in session: ' + session['email'] + '</h1>'
#    else:
#        str='<h1>No email  in session</h1>'
#    return str
#    return render_template('index.html')

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

#@mainbp.route('/login', methods=['GET','POST'])#route name with
#def login(): # view function
#    session['email'] = request.values.get('email')
#    print(request.values.get('email'))
#    print(request.values.get('pwd'))
#    return render_template('login.html')


#@mainbp.route('/logout')
#def logout():
#    if 'email' in session:
#        session.pop('email', None)
#        return 'Session has been cleared'

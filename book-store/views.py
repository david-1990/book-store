from flask import Blueprint, render_template, request, session

mainbp = Blueprint('main',__name__)

@mainbp.route('/', methods=['GET','POST'])
def index():
    # if 'email' in session:
    #     str = '<h1>Hello world ' + session['email'] + '</h1>'
    # else:
    #     str = '<h1>Hello</h1>'
    return render_template('index.html')

@mainbp.route('/login', methods=['GET','POST'])
def login():
    #print(request.values.get('email'))
    #print(request.values.get('pwd'))
    session['email']=request.values.get('email')
    return render_template('login.html')

@mainbp.route('/logout', methods=['GET','POST'])
def logout():
    if 'email' in session:
        session.pop('email', None)
    return 'Session has been cleared'
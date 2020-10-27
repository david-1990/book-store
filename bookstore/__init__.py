from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    print(__name__)
    app = Flask(__name__)

    app.secret_key='fG5Hj#tt!hUiFC4'

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///bookstore.sqlite'
    db.init_app(app)

    bootstrap = Bootstrap(app)

    from . import views
    app.register_blueprint(views.mainbp)

    return app
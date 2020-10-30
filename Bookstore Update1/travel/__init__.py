# import flask - from the package import a module
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

# create a function that creates a web application
# a web server will run this web application

#create a user loader function takes userid and returns User

def create_app():
    # this is the name of the module/package that is calling this app
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'anythingyoulike'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel123.sqlite'
    db.init_app(app)

    from .models import User # importing here to avoid circular references
    # initialize the login manager

    bootstrap = Bootstrap(app)
    
    from .models import User # importing here to avoid circular references
    # initialize the login manager
    login_manager = LoginManager()

    # set the name of the login function that lets user login. in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from . import views
    app.register_blueprint(views.mainbp)

    from . import items
    app.register_blueprint(items.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    # initialize the login manager
    login_manager = LoginManager()

    # set the name of the login function that lets user login. in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    #create a user loader function takes userid and returns User
    from .models import User # importing here to avoid circular references
    @login_manager.user_loader
    
    def load_user(user_id):
        return User.query.get(int(user_id))
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    return app



if __name__ == '__main__':
    napp = create_app()
    napp.run(debug=True)


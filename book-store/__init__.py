from flask import Flask

def create_app():
    print(__name__)
    app = Flask(__name__)

    from . import views
    app.register_blueprint(views.mainbp)

    app.secret_key='anythingyoulike'

    return app
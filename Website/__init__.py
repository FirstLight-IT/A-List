from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def getApp():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = "TeamFirstLight"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'routes.login'
    login_manager.login_message = "You must log in to access this page."
    login_manager.login_message_category = "error"


    from .models import User
    from .routes import bp
    app.register_blueprint(bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

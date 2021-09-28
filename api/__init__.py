from instance.config import DevelopmentConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    from api.route import home
    app.register_blueprint(home.home)

    return app
from flask import Flask, Blueprint
from flask_migrate import Migrate
from .views import main
from config import app_config
from .extensions import db


def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(main)
    return app

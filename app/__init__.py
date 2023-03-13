from flask import Flask
from .config import config
from app.Accounts import accounts as accounts_blueprint
from app.main import main as main_blueprints
from .extensions import login_manager, custom_bcrypt


## load here all internal applications and register them and inside the __init__ of each one create a blueprint
def create_app(config_name="default"):

    app = Flask(__name__)
    # 1- configuration, settings
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 2- extensions (db,login,..)
    login_manager.init_app(app)
    custom_bcrypt.init_app(app)
    # mongo.init_app(app)

    # 3- blueprints
    app.register_blueprint(accounts_blueprint)
    app.register_blueprint(main_blueprints)

    return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy, create_engine
from .config import App_Config
from flask_caching import Cache 

db = SQLAlchemy()
cache = Cache() 

def create_app():
    app = Flask(__name__)
    app.config.from_object(App_Config)
    if app.config["SQLALCHEMY_DATABASE_URI"]:
        print("using db")

    cache.init_app(app)
    db.init_app(app)

    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], pool_pre_ping=True, pool_recycle=300)

    from Newton_Breakout.routes import game

    app.register_blueprint(game)

    with app.app_context():
        db.create_all()
    return app
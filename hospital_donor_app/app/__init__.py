from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import secrets
import pymysql

# Initialize extensions (without binding to the app)
db = SQLAlchemy()
jwt = JWTManager()

# This will store the singleton app instance
app = None
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure your database
    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://santhoshtk:Blms0011@blms-database.c3s8q0cewlnq.eu-north-1.rds.amazonaws.com:3306/mydatabase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_size': 10,
        'pool_recycle': 280,
        'pool_timeout': 30,
        'max_overflow': 5,
        'echo': True
    }

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate with the app and db

    # Register blueprints or other app logic
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

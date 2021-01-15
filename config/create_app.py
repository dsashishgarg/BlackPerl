from flask import Flask, jsonify
from app.product.db import db
from flask_restplus import Api


def create_app(env=None):
    from app.product.routes import register_routes

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True

    api = Api(app, title="BlackPerl")

    register_routes(api, app)

    # creating all req tables
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app

# Copyright (c) 2022, Ansys Inc. Unauthorised use, distribution or duplication is prohibited

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
import argparse
import logging
from src.blueprints.version import blueprint as version_endpoint
from src.blueprints.health import blueprint as health_endpoint


SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'


SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Name"
    }
)


def create_app():
    """Initialize the core application"""
    app = Flask(__name__)
    CORS(app, resources=r'/api/*')
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.register_blueprint(version_endpoint)
    app.register_blueprint(health_endpoint)
    app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

    return app


def serve(app, address, port, middleware=None):

    if middleware is not None:
        middleware(app)

    logging.info('Server flask starting')
    app.run(host=address, port=port)


if __name__ == '__main__':
    app = create_app()
    logging.info('server.py main : parsing arguments')
    parser = argparse.ArgumentParser()
    parser.add_argument("--address",
                        help="Set server address",  )
    parser.add_argument("-v", "--port", type=int,
                        help="Set server port", default=5000)
    args = parser.parse_args()
    serve(app=app, address=args.address, port=args.port)

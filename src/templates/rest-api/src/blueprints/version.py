from flask import Blueprint, jsonify

blueprint = Blueprint('api_version', __name__, url_prefix='/api/version')


@blueprint.route('/')
def get_version():
    return jsonify({'version': '1.0.0'})
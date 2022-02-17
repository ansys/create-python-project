from flask import Blueprint, request, jsonify
import logging
blueprint = Blueprint('health_check', __name__, url_prefix='/api/health')


@blueprint.route('/')
def health_check():
    logging.info('Health check')
    return jsonify({'status': 'ok'})
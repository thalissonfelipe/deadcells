import json
from flask import Blueprint, Response, current_app


bp = Blueprint('outfits', __name__)


@bp.route('/outfits')
def get_outfits():
    response = Response(response='OK', status=200)
    try:
        data = current_app.scrapper_manager.get('outfits')
        if data is None:
            data = current_app.scrapper_manager.get_outfits()
            current_app.scrapper_manager.insert(data)
        response.data = json.dumps(data['data'])
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/outfits/<name>')
def get_outfit_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = current_app.scrapper_manager.get('outfits')
        if data is None:
            data = current_app.scrapper_manager.get_outfits()
            current_app.scrapper_manager.insert(data)
        for outfit in data['data']:
            if outfit['name'] == name:
                response.data = json.dumps(outfit)
                response.mimetype = 'application/json'
                name_exists = True
                break
        if not name_exists:
            response.data, response.status_code = 'Outfit not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

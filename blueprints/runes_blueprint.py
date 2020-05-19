import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('runes', __name__)


@bp.route('/runes')
def get_runes():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_runes())
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/runes/<name>')
def get_rune_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = Scrapper().get_runes()
        for rune in data:
            if rune['name'] == name:
                response.data = json.dumps(rune)
                response.mimetype = 'application/json'
                name_exists = True
                break
        if not name_exists:
            response.data, response.status_code = 'Rune not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('enemies', __name__)


@bp.route('/enemies')
def get_enemies():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_enemies())
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/enemies/<name>')
def get_enemy_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = Scrapper().get_enemies()
        for enemy in data:
            if enemy['name'] == name:
                response.data = json.dumps(enemy)
                response.mimetype = 'application/json'
                name_exists = True
                break
        if not name_exists:
            response.data, response.status_code = 'Enemy not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

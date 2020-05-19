import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('bosses', __name__)


@bp.route('/bosses')
def get_bosses():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_bosses())
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/bosses/<name>')
def get_boss_by_name(name):
    response = Response(response='OK', status=200)
    try:
        data = Scrapper().get_boss(name)
        if data:
            response.data = json.dumps(data)
            response.mimetype = 'application/json'
        else:
            response.data, response.status_code = 'Boss not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

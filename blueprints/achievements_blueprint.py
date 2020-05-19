import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('achievements', __name__)


@bp.route('/achievements')
def get_achievements():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_achievements())
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/achievements/<name>')
def get_achievement_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = Scrapper().get_achievements()
        for achievement in data:
            if achievement['name'] == name:
                response.data = json.dumps(achievement)
                response.mimetype = 'application/json'
                name_exists = True
                break
        if not name_exists:
            response.data, response.status_code = 'Achievement not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

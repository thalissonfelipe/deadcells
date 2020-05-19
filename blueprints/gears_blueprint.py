import json
from flask import Blueprint, Response, current_app


bp = Blueprint('gears', __name__)


@bp.route('/gears')
def get_gears():
    response = Response(response='OK', status=200)
    try:
        data = current_app.scrapper_manager.get('gears')
        if data is None:
            data = current_app.scrapper_manager.get_gears()
            current_app.scrapper_manager.insert(data)
        response.data = json.dumps(data['data'])
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/gears/type/<type>/')
def get_gears_by_type(type):
    response = Response(response='OK', status=200)
    try:
        types = [
            'malee_weapons', 'ranged_weapons', 'shields',
            'traps_and_turrets', 'grenades', 'powers', 'amulets'
        ]
        if type not in types:
            response.data, response.status_code = 'Invalid gear type.', 400
        else:
            data = current_app.scrapper_manager.get('gears')
            if data is None:
                data = current_app.scrapper_manager.get_gears()
                current_app.scrapper_manager.insert(data)
            data = data['data'][types.index(type)]
            response.data = json.dumps(data)
            response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/gears/name/<name>')
def get_gear_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = current_app.scrapper_manager.get('gears')
        if data is None:
            data = current_app.scrapper_manager.get_gears()
            current_app.scrapper_manager.insert(data)
        for weapon_type in data['data']:
            for gear in weapon_type['gears']:
                if gear['name'] == name:
                    gear['type'] = weapon_type['type']
                    response.data = json.dumps(gear)
                    response.mimetype = 'application/json'
                    name_exists = True
                    break
        if not name_exists:
            response.data, response.status_code = 'Gear not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

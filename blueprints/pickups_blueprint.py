import json
from flask import Blueprint, Response, current_app


bp = Blueprint('pickups', __name__)


@bp.route('/pickups')
def get_pickups():
    response = Response(response='OK', status=200)
    try:
        data = current_app.scrapper_manager.get('pickups')
        if data is None:
            data = current_app.scrapper_manager.get_pickups()
            current_app.scrapper_manager.insert(data)
        response.data = json.dumps(data['data'])
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/pickups/type/<type>')
def get_pickups_by_type(type):
    response = Response(response='OK', status=200)
    try:
        types = ['gems', 'minor_foods', 'major_foods', 'scrolls', 'keys']
        if type not in types:
            response.data, response.status_code = 'Invalid pickup type.', 400
        else:
            data = current_app.scrapper_manager.get('pickups')
            if data is None:
                data = current_app.scrapper_manager.pickups()
                current_app.scrapper_manager.insert(data)
            data = data['data'][types.index(type)]
            response.data = json.dumps(data)
            response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/pickups/name/<name>')
def get_pickup_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = current_app.scrapper_manager.get('pickups')
        if data is None:
            data = current_app.scrapper_manager.get_pickups()
            current_app.scrapper_manager.insert(data)
        for pickup_type in data['data']:
            for pickup in pickup_type['pickups']:
                if pickup['name'] == name:
                    pickup['type'] = pickup_type['type']
                    response.data = json.dumps(pickup)
                    response.mimetype = 'application/json'
                    name_exists = True
                    break
        if not name_exists:
            response.data, response.status_code = 'Pickup not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

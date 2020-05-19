import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('pickups', __name__)


@bp.route('/pickups')
def get_pickups():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_pickups())
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
        types = ['gems', 'minor_food', 'major_food', 'scrolls', 'keys']
        if type not in types:
            response.data, response.status_code = 'Invalid pickup type.', 400
        else:
            data = Scrapper().get_pickups()[types.index(type)]
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
        data = Scrapper().get_pickups()
        for pickup_type in data:
            for pickup in pickup_type['pickups']:
                if pickup['name'] == name:
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

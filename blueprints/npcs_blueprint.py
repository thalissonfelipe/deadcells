import json
from flask import Blueprint, Response, current_app


bp = Blueprint('npcs', __name__)


@bp.route('/npcs')
def get_npcs():
    response = Response(response='OK', status=200)
    try:
        data = current_app.scrapper_manager.get('npcs')
        if data is None:
            data = current_app.scrapper_manager.get_npcs()
            current_app.scrapper_manager.insert(data)
        response.data = json.dumps(data['data'])
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/npcs/<name>')
def get_npc_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = current_app.scrapper_manager.get('npcs')
        if data is None:
            data = current_app.scrapper_manager.get_npcs()
            current_app.scrapper_manager.insert(data)
        for npc in data['data']:
            if npc['name'] == name:
                response.data = json.dumps(npc)
                response.mimetype = 'application/json'
                name_exists = True
                break
        if not name_exists:
            response.data, response.status_code = 'NPC not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

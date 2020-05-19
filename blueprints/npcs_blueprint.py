import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('npcs', __name__)


@bp.route('/npcs')
def get_npcs():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_npcs())
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
        data = Scrapper().get_npcs()
        for npc in data:
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

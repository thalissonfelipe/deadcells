import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('biomes', __name__)


@bp.route('/biomes')
def get_biomes():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_biomes())
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/biomes/<name>')
def get_biome_by_name(name):
    response = Response(response='OK', status=200)
    try:
        data = Scrapper().get_biome(name)
        if data:
            response.data = json.dumps(data)
            response.mimetype = 'application/json'
        else:
            response.data, response.status_code = 'Biome not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

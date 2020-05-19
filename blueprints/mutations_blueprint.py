import json
from flask import Blueprint, Response, current_app


bp = Blueprint('mutations', __name__)


@bp.route('/mutations')
def get_mutations():
    response = Response(response='OK', status=200)
    try:
        data = current_app.scrapper_manager.get('mutations')
        if data is None:
            data = current_app.scrapper_manager.get_mutations()
            current_app.scrapper_manager.insert(data)
        response.data = json.dumps(data['data'])
        response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/mutations/type/<type>')
def get_mutations_by_type(type):
    response = Response(response='OK', status=200)
    try:
        types = ['brutality', 'tactics', 'survival', 'colorless']
        if type not in types:
            response.data, response.status_code = 'Invalid mutation type.', 400
        else:
            data = current_app.scrapper_manager.get('mutations')
            if data is None:
                data = current_app.scrapper_manager.get_mutations()
                current_app.scrapper_manager.insert(data)
            data = data['data'][types.index(type)]
            response.data = json.dumps(data)
            response.mimetype = 'application/json'
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response


@bp.route('/mutations/name/<name>')
def get_mutation_by_name(name):
    response = Response(response='OK', status=200)
    try:
        name_exists = False
        data = current_app.scrapper_manager.get('mutations')
        if data is None:
            data = current_app.scrapper_manager.get_mutations()
            current_app.scrapper_manager.insert(data)
        for mutation_type in data['data']:
            for mutation in mutation_type['mutations']:
                if mutation['name'] == name:
                    mutation['type'] = mutation_type['type']
                    response.data = json.dumps(mutation)
                    response.mimetype = 'application/json'
                    name_exists = True
                    break
        if not name_exists:
            response.data, response.status_code = 'Mutation not found.', 404
    except Exception as e:
        current_app.logger.exception(e)
        response.data, response.status_code = 'Internal Server Error.', 500
    finally:
        return response

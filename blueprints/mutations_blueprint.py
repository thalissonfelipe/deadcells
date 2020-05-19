import json
from scrapper import Scrapper
from flask import Blueprint, Response, current_app


bp = Blueprint('mutations', __name__)


@bp.route('/mutations')
def get_mutations():
    response = Response(response='OK', status=200)
    try:
        response.data = json.dumps(Scrapper().get_mutations())
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
        types = ['brutality', 'tatic', 'survival', 'colorless']
        if type not in types:
            response.data, response.status_code = 'Invalid mutation type.', 400
        else:
            data = Scrapper().get_mutations()[types.index(type)]
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
        data = Scrapper().get_mutations()
        for mutation_type in data:
            for mutation in mutation_type['mutations']:
                if mutation['name'] == name:
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

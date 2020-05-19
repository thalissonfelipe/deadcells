# /usr/bin/python3
__author__ = 'Thalisson Sousa'

from flask import Flask
from flask_cors import CORS
from scrapper import Scrapper


def create_app():
    app = Flask(__name__)
    CORS(app)

    from blueprints import npcs_blueprint
    from blueprints import gears_blueprint
    from blueprints import runes_blueprint
    from blueprints import biomes_blueprint
    from blueprints import bosses_blueprint
    from blueprints import outfits_blueprint
    from blueprints import pickups_blueprint
    from blueprints import enemies_blueprint
    from blueprints import mutations_blueprint
    from blueprints import achievements_blueprint

    app.register_blueprint(npcs_blueprint.bp)
    app.register_blueprint(gears_blueprint.bp)
    app.register_blueprint(runes_blueprint.bp)
    app.register_blueprint(biomes_blueprint.bp)
    app.register_blueprint(bosses_blueprint.bp)
    app.register_blueprint(outfits_blueprint.bp)
    app.register_blueprint(pickups_blueprint.bp)
    app.register_blueprint(enemies_blueprint.bp)
    app.register_blueprint(mutations_blueprint.bp)
    app.register_blueprint(achievements_blueprint.bp)

    app.scrapper_manager = Scrapper()

    @app.errorhandler(404)
    def route_not_found(error):
        app.logger.error(error)
        return 'Route not found.', 404

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(
        debug=True,
        host='192.168.0.100',
        threaded=True
    )

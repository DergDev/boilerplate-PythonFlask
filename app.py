import logging
import urllib3
from flask import Flask
from flasgger import Swagger
from api.route.health import health_api


def create_app():
    global app
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'BOILERPLATE API SWAGGER',
        'description': 'NONE.',
        'contact': {
            'responsibleOrganization': 'https://www.seela.io/',
            'responsibleDeveloper': 'NONE'
        }
    }
    # initialize the app with the extension
    # Usage outside scope. Ignore warning.
    swagger = Swagger(app)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    urllib3.disable_warnings()
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.config.from_pyfile('config.py')
    app.register_blueprint(health_api, url_prefix='/')
    return app


if __name__ == '__main__':
    global app
    # Usage outside scope. Ignore warning.
    app = create_app()
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0')

from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from

from api.model.default_models import DefaultHealthResponse
from api.schema.default_schemas import DefaultHealthResponseSchema
from api.utils.wsgi_logging import LoggingUtility

health_api = Blueprint('/', __name__)


@health_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK: {
            'description': 'Returns the state of the API',
        }
    },
    'tags': ['Health']
})
def health():
    """
    Returns a status about the API health.
    The API will wait for the query and returns an OK or an ERROR.
    ---
    """
    payload_model = DefaultHealthResponse()
    payload_schema_dump = DefaultHealthResponseSchema().dump(payload_model)
    LoggingUtility.debug('Health: OK.')
    return payload_schema_dump, 200

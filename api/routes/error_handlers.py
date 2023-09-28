from flask import Blueprint
from ..models.exceptions import NotFound, InvalidDataError

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(NotFound)
def handle_film_not_found(error):
    return error.get_response(), error.status_code


@errors.app_errorhandler(InvalidDataError)
def handle_ivalid_data_error(error):
    return error.get_response(), error.status_code
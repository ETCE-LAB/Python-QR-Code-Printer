from flask import jsonify
from werkzeug.exceptions import HTTPException


class CustomError(HTTPException):
    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code or 500
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    def get_response(self, environ=None):
        response = jsonify(self.to_dict())
        response.status_code = self.status_code
        return response


def handle_custom_error(e):
    response = e.get_response()
    response.status_code = e.status_code
    return response

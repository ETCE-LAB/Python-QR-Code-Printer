import logging
import traceback
from flask import jsonify, make_response
from errors.errors import CustomError
from services.services import create_qr_code, print_qr_code

logger = logging.getLogger(__name__)


def handle_print_request(data, text):
    try:
        qr_image = create_qr_code(data, id_text=text, name_text=data)
        response, status_code = print_qr_code(qr_image)
        return make_response(jsonify(response), status_code)
    except CustomError as e:
        logger.error(f"Error: {e}")
        logger.error(traceback.format_exc())
        return make_response(jsonify({"error": e.message}), e.status_code)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.error(traceback.format_exc())
        return make_response(jsonify({"error": f"Unexpected error: {e}"}), 500)

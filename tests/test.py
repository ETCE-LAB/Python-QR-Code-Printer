import unittest
from flask import jsonify
from flask_testing import TestCase
from unittest.mock import patch, MagicMock
from PIL import ImageFont, ImageDraw

# Import your app and necessary modules
from app import app
from utils.helpers import handle_print_request
from services.services import create_qr_code, print_qr_code
from errors.errors import CustomError


class TestPrintAPI(TestCase):
    def create_app(self):
        return app

    def test_create_qr_code(self):
        with patch('services.services.load_font', return_value=MagicMock(spec=ImageFont.FreeTypeFont)):
            data = "test_data"
            text = "test_text"
            qr_code_mock = MagicMock()
            qr_code_mock.width = 100
            qr_code_mock.height = 100
            with patch('services.services.qrcode.QRCode.make_image', return_value=qr_code_mock):
                draw_mock = MagicMock()
                draw_mock.textbbox.return_value = (0, 0, 50, 10)
                with patch('services.services.ImageDraw.Draw', return_value=draw_mock):
                    image = create_qr_code(data, text)
                    self.assertIsNotNone(image)

    def test_print_qr_code(self):
        with patch('services.services.resize_image',
                   return_value=MagicMock(width=500, height=500)) as mock_resize_image, \
                patch('services.services.convert', return_value=None) as mock_convert, \
                patch('services.services.send', return_value=None) as mock_send, \
                patch('PIL.Image.new', return_value=MagicMock()) as mock_image_new:
            image = MagicMock()
            response, status_code = print_qr_code(image)
            self.assertEqual(status_code, 200)
            self.assertIn('status', response)
            self.assertEqual(response['status'], "Print successfully completed")

    def test_print_resource(self):
        with patch('utils.helpers.handle_print_request', return_value=(
        jsonify({"status": "Print successfully completed"}), 200)) as mock_handle_print_request:
            response = self.client.post('/print/test_uuid/test_name')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['status'], "Print successfully completed")

    def test_debug_print_resource(self):
        with patch('utils.helpers.handle_print_request', return_value=(
        jsonify({"status": "Debug print successfully completed"}), 200)) as mock_handle_print_request:
            response = self.client.post('/print/debug/print')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['status'], "Debug print successfully completed")

    def test_custom_error(self):
        @app.route('/test_custom_error')
        def test_custom_error_route():
            raise CustomError("This is a custom error", status_code=418)

        response = self.client.get('/test_custom_error')
        self.assertEqual(response.status_code, 418)
        self.assertEqual(response.json['message'], "This is a custom error")


if __name__ == '__main__':
    unittest.main()

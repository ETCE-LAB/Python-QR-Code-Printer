from flask import Flask
from flask_restx import Api
from printer_api.api import ns
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app, version='1.0', title='Print API', description='A simple API for printing QR codes')

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

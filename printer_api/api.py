from flask_restx import Api, Resource
from utils.helpers import handle_print_request

api = Api(version='1.0', title='Print API', description='A simple API for printing QR codes')
ns = api.namespace('print', description='Printing operations')


@ns.route('/<string:uuid>/<string:name>')
class PrintResource(Resource):
    @api.doc(responses={200: 'Print successfully completed', 400: 'Invalid input', 424: 'Error preparing image',
                        503: 'Printer not connected'})
    def post(self, uuid, name):
        return handle_print_request(uuid, name)


@ns.route('/debug/print')
class DebugPrintResource(Resource):
    @api.doc(responses={200: 'Debug print successfully completed', 424: 'Error preparing image',
                        503: 'Printer not connected'})
    def post(self):
        fixed_string = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
        fixed_text = "Hier könnte Ihre Werbung stehen!"
        return handle_print_request(fixed_string, fixed_text)

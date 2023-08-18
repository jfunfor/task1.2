from flask_restful import Api

from ..main.controllers.kValues_controller import KeyValue, KeyValueList



def create_api():
    api = Api()
    api.add_resource(KeyValueList, '/api/v1/storage/json/all')
    api.add_resource(KeyValue, *['/api/v1/storage/json/write', '/api/v1/storage/json/<string:item_id>'])
    return api

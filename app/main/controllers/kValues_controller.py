from flask import request
from flask_restful import Resource
from ..services.kValues_service import add_item_to_file, read_all_file, read_by_key


class KeyValue(Resource):
    def get(self, item_id):
        return read_by_key(item_id)

    def post(self):
        postdata = request.get_json()
        return add_item_to_file(postdata)


class KeyValueList(Resource):
    def get(self):
        return read_all_file()

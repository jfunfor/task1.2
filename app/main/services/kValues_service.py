import json
import tempfile

tmp = tempfile.NamedTemporaryFile(mode='r+t',
                                  prefix='task1.2_',
                                  dir='/tmp',
                                  delete=True)

def add_item_to_file(data):
    try:
        tmp.seek(0)
        if len(list(data.keys())) > 1:
            return {"info": "Please add one item per request"}, 400
        if len(tmp.read()) == 0:
            json.dump(data, tmp)
            return {"info": "Item was successfully added to the new key"}, 200
        else:
            tmp.seek(0)
            storage = json.load(tmp)
            if not list(data.keys())[0] in list(storage.keys()):
                storage[list(data.keys())[0]] = data[list(data.keys())[0]]
                tmp.seek(0)
                tmp.truncate()
                json.dump(storage, tmp)
                tmp.seek(0)
                return {"info": "Item was successfully added to the new key"}
            else:
                tmp.seek(0)
                storage[list(data.keys())[0]] += "," + data[list(data.keys())[0]]
                tmp.truncate()
                json.dump(storage, tmp)
                tmp.seek(0)
                tmp.read()
                return {"info": "Item was successfully added to the existing key"}
    except Exception:
        return {"info": "Something went wrong. Please try again"}, 500


def read_all_file():
    try:
        tmp.seek(0)
        if len(tmp.read()) == 0:
            return {"info": "Storage is empty. Please add something first"}, 200
        else:
            tmp.seek(0)
            storage = json.load(tmp)
            return storage
    except Exception:
        return {"info": "Something went wrong. Please try again"}, 500


def read_by_key(item_id):
    try:
        tmp.seek(0)
        if len(tmp.read()) == 0:
            return {"info": "Storage is empty. Please add something first"}, 200
        tmp.seek(0)
        storage = json.load(tmp)
        if len(list(storage.keys())) == 0:
            return {"info": "Storage is empty. Please add something first"}, 200
        elif item_id not in storage.keys():
            return {"info": "No such item in storage"}
        else:
            return {f'{item_id}': f'{storage[item_id]}'}
    except Exception:
        return {"info": "Something went wrong. Please try again"}, 500

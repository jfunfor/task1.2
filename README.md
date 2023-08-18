Prototype of API storage key-value

Get all data of WEB-storage:
http://{HOSTNAME:PORT}/api/v1/storage/json/all

Get all data of CURL-storage:
curl -i -X GET http://{HOSTNAME:PORT}/api/v1/storage/json/all

Get data of WEB-storage by key:
http://{HOSTNAME:PORT}/api/v1/storage/json/<string:item_id>

Get data of WEB-storage by key:
curl -i -X GET http://{HOSTNAME:PORT}/api/v1/storage/<string:item_id>

Post data in Web-storage:
curl -i -H "Content-Type:application/json" -X POST -d '{"test3":"value4"}' http://{HOSTNAME:PORT}/api/v1/storage/json/write
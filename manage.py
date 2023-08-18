from app.main import create_app
from app.api import create_api
from flask import Response, render_template

app = create_app('dev')
api = create_api()
api.init_app(app)

@app.route('/')
def hello_world():
    r = Response(open('README.md').read(), mimetype="text/plain")
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

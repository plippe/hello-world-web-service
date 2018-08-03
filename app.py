import os
from flask import Flask

def hello(path=None):
    return 'Hello from /%s!' % (path or '')

def toInt(num):
    try:
        return int(num)
    except:
        return None

if __name__ == '__main__':
    port=toInt(os.getenv('FLASK_PORT'))

    # https://tools.ietf.org/html/rfc7231#section-4.1
    methods = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']

    app = Flask(__name__)
    app.add_url_rule('/', 'hello', hello, methods=methods)
    app.add_url_rule('/<path:path>', 'hello', hello, methods=methods)
    app.run(host='0.0.0.0', port=port)

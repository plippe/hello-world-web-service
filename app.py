import os, json
from flask import Flask, request

def hello(path=None):
    req = json.dumps({
        'method': request.method,
        'url': request.url,
        'headers': request.headers.to_list(),
        'path': request.path,
        'args': request.args,
        'form': request.form,
        'data': request.data.decode("utf-8"),
    })

    print(req)
    return req

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

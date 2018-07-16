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

    app = Flask(__name__)
    app.add_url_rule('/', 'hello', hello)
    app.add_url_rule('/<path:path>', 'hello', hello)
    app.run(host='0.0.0.0', port=port)

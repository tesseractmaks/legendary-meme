import json
import os

# from wsgiref import simple_server



# class Application(object):
#     def __call__(self, environ, start_response):
#         if environ['PATH_INFO'] == '/hello':
#             return self.hello(environ, start_response)
#         elif environ['PATH_INFO'] == '/hello/username':
#             return self.hello_user(environ, start_response)
#         else:
#             start_response('404 Not Found', [('Content-type', 'text/html')])
#             return [b'404 Not Found']
#
#     def hello(self, environ, start_response):
#         start_response('200 OK', [('Content-type', 'application/json')])
#         json_data = json.dumps([{'message': 'Hello'}]).encode("utf-8")
#         return [json_data]
#
#     def hello_user(self, environ, start_response):
#         start_response('200 OK', [('Content-type', 'application/json')])
#         username = environ['USERNAME']
#         json_data = json.dumps([{'message': 'Hello', 'user': username}]).encode("utf-8")
#         return [json_data]


# app = Application()

# httpd = simple_server.WSGIServer(
#     ('0.0.0.0', 8001),
#     simple_server.WSGIRequestHandler,
# )
# httpd.set_app(app)
# httpd.serve_forever()
from markupsafe import escape
from flask import Flask, jsonify, make_response, send_from_directory, url_for, send_file, Response, render_template

app = Flask(__name__)

# app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world(username='username'):
    return make_response(jsonify(message='hello', name=username))


@app.route('/static/<path:path>')
def serve_static(path):
    file = os.path.join('static', path)
    # print(file)
    # return send_from_directory('static', path)
    # return render_template('index.html', image=path)
    return render_template('index.html', image=file)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=80)
    # app.run(host="0.0.0.0", debug=True)


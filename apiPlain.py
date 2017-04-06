#!/usr/bin/env python
from flask import Flask,request,jsonify
from gevent.wsgi import WSGIServer
from os import environ
# environ.get('PORT')
app = Flask(__name__)
@app.route('/')
def get():
	return jsonify('Hello, World!')

	
if __name__ == '__main__':
         #app.run(environ.get('PORT'))
         http_server = WSGIServer(('0.0.0.0', 5000), app)
         http_server.serve_forever()






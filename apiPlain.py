#!/usr/bin/env python
from flask import Flask,request,jsonify
from gevent.wsgi import WSGIServer

@app.route('/')
def get():
	return jsonify('Hello, World!')

	
if __name__ == '__main__':
	http_server = WSGIServer(('0.0.0.0', 5050), app)
    http_server.serve_forever()






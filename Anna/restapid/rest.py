#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__) # __name__ - name of file, reserved one
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':  #if smb use console -> open app
    app.run(debug=True)

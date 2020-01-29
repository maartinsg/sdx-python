#!/usr/bin/env python

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__) # __name__ - name of file, reserved one/ initialize flask(server)
api = Api(app) #initialize api(handler for the requests)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':  #if smb use console -> open app
    app.run(debug=True)

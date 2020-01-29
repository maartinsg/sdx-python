#!/usr/bin/env python

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

#todo list
#shows a list of all todos and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id ='todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        print("sebug: added task with id '{}'".format(todo_id))
        return TODOS[todo_id], 201

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'}
}

app = Flask(__name__) # __name__ - name of file, reserved one/ initialize flask(server)
api = Api(app) #initialize api(handler for the requests)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList, '/todos')

if __name__ == '__main__':  #if smb use console -> open app
    app.run(debug=True)

#!/usr/bin/env python

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

#todo list
#shows a list of all todos and lets you POST to add new tasks / collection 
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

# shows a single todo item and lets you delete a todo item /elements
class Todo(Resource):
    def get(self, todo_id):
        #abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'}
}

app = Flask(__name__) # __name__ - name of file, reserved one/ initialize flask(server)
api = Api(app) #initialize api(handler for the requests)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':  #if smb use console -> open app
    app.run(debug=True)

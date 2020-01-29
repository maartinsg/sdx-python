#!/usr/bin/env python
from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

# TodoList
# Shows a list of all todos, and lets you POST to add new tasks


class TodoSimple(Resource):
    def get(self):
        print("debug: sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        print("debug: added task with id '{}'".format(todo_id))
        return TODOS[todo_id], 201
    
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'destroy an API'},
}
    
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

##Setup the API resource routing here

api.add_resource(TodoSimple, '/todos')

if __name__ == '__main__':
    app.run(debug=True)

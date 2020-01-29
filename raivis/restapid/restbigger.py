#!/usr/bin/env python
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

# TodoList

class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        print("devug: added task with id '{}'".format(todo_id))
        return TODOS[todo_id], 201

class Todo(Resource):
    def get(self, todo_id):
        #abort_if_todo_doesnt_exit(todo_id)
        return TODOS[todo_id]

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
    
TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'be a pro'},
}


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

##
## Actually set up API resource routing here
##
api.add_resource(TodoList, '/TODOS')
api.add_resource(Todo, '/TODOS/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

#!/user/bin/env python
from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
app = Flask(__name__)
api = Api(app)

    
TODOS = {
    'todo1': {'task': 'build an API'),
    'todo2': {'task': '?????'),
    }
parser = reqparse.RequestPaeser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo__doesnt_exist(todo_id)
        return TODOS[todo_id]
    
     def delete(self, todo_id):
        print("debug: deleting task with id '[]'".format(todo_id))
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        print("debug: added task with id '{}'".format(todo_id))
        return TODO[todo_id], 201




api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True)



api.add_resource(Tdo, '/todos/<todo_id>')



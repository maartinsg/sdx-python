####################
##    REST API    ##
####################
## use this line to run the file using Python #!/usr/bin/env python

#!/usr/bin/env python

from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api


class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return todos

    def put(self):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = {'task': args['task']}
        print("debug: added task with id '{}'".format(todo_id))
        return todos[todo_id], 201

class Todo(Resource):
    def get(self, todo_id):
##        abort_if_todo_doesnt_exist(todo_id)
        return todos[todo_id]

    def delete(self, todo_id):
        print("debug: deleting task with id '{}'".format(todo_id))
##        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        todos[todo_id] = task
        return task, 201

todos = {
    'todo1': {'task': 'doing something 1'},
    'todo2': {'task': 'doing something 2'},   
    'todo3': {'task': 'doing something 3'},
    'todo4': {'task': 'doing something 4'},
    'todo5': {'task': 'doing something 5'},
        }
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
##    app.run(debug=True)


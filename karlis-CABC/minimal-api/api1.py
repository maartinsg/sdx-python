#!/user/bin/env python
from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from subprocess import Popen, PIPE

# TodoList
# show a list of all todos, and lets you POST to add new tasks
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
        return TODOS[todo_id], 201
# Todoo
# Shows a sinlge todoo item and lets you delete a todoo item
class Ping(Resource):
    def get(self, ip):
        print ("debug ping IP '()'".format(ip))
        process = Popen(" ".join(['ping', ip, '-c', '1']),
            shell=True, stdout=PIPE, stderr=PIPE)

        out = process.stdout.read()
        print ("STDOUT: ({})".format(out))

        rc = process.wait()
        print ("exit code: ({})".format(rc))

        return out


class Todo(Resource):
    def get(self, todo_id):
        print("debug: getting task with id '{}'".format(todo_id))
        # abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        print("debug: deleting task with id '{}'".format(todo_id))
        # abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        print("debug: creating task with id '{}'".format(todo_id))
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


TODOS = {
    'task1': {'task': 'build an API'},
    'todo2': {'task': 'eat cake'},
}

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

# Actually setup the Api resource routing here

api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(Ping, '/ping/<ip>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


#!/usr/bin/env python
from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from subprocess import Popen, PIPE

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

# Todo
# shows a single todo item and lets you delete a todo item

class Todo(Resource):
    def get(self, todo_id):
        #abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        print("debug: deleting task with id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class Ping(Resource):
    def get(self, ip):
        print ("debug: ping IP '{}'".format(ip))
        # execute com mand
        process = Popen(" ".join(
            ['ping', ip,'-c' 'l']),
            shell=True, stdout=PIPE, stderr=PIPE)

        # read stdout
        out = process.stdout.read()
        print("STDOUT: {}".format(out))

        # wait for child process to terminate.
        rc = process.wait()
        print ("exit code: {}".format(rc))
        return out



##Setup the API resource routing here

api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(TodoSimple, '/todos')

api.add_resource(Ping, '/ping/<ip>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
#192.168.8.107

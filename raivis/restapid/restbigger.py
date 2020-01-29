#!/usr/bin/env python
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from subprocess import Popen, PIPE

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
        print("debug: getting task with id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exit(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        print("debug: getting task with id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exit(todo_id)
        del TODOS[todo_id]
        return '', 204
    
    def put(self, todo_id):
        print("debug: getting task with id '{}'".format(todo_id))
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class Ping(Resource):
    def get(self, ip_adress):
        print("debug: getting ip address '{}'".format(ip_adress))
        process = Popen(" ".join(['ping', ip_adress, '-c', '1']),
                    shell=True, stdout=PIPE, stderr=PIPE)
        out = process.stdout.read()
        print("STDOUT: {}".format(out))
        rc = process.wait()
        print("exit code: {}".format(rc))
        return out


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'be a pro'},
}


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('ping')

##
## Actually set up API resource routing here
##
api.add_resource(TodoList, '/TODOS')
api.add_resource(Todo, '/TODOS/<todo_id>')
api.add_resource(Ping, '/PING/<ip_adress>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

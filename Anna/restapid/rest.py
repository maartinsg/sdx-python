#!/usr/bin/env python

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from subprocess import Popen, PIPE

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

# shows a single todo item and lets you delete a todo item / elements
class Todo(Resource):
    def get(self, todo_id):
        print("debug: gitting task with id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        print("debug: deleting task with id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        print("debug: creating task with id '{}'".format(todo_id))
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

class Ping(Resource):
    def get(self, ip):
        print("debug: ping IP '{}'".format(ip))
        process = Popen (" ".join(['ping', ip, '-c', '2']),
                         shell=True, stdout=PIPE, stderr=PIPE)

        out = process.stdout.read()
        print("stdout: {}".format(out))

        rc =process.wait()
        print("exit code: {}".format(rc))

        return out

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
api.add_resource(Ping, '/ping/<ip>')

if __name__ == '__main__':  #if smb uses console -> open app
    app.run(debug=True, host='0.0.0.0', port='5000')

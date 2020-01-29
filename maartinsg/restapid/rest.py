#!/usr/bin/env python

####################
# RestAPI
####################
from subprocess import Popen, PIPE
from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

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

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'}
}

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

## actually setting up the Api resource routing here
#api.add_resource(TodoList, '/todos')

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(selfself, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

# return Dictionary part
######api.add_resource(TodoSimple, '/todos')

class Ping(Resource):
    def get(self, ip):
        print("debug: ping IP '{}'".format(ip))
        process = Popen(" ".join(['ping', '-c', '2', ip]), shell=True, stdout=PIPE, stderr=PIPE)
        #print(processing)
        #read STDOUT
        out = process.stdout.read()
        #wait for the subprocess to finish?
        rc = process.wait()
        print("exit code: {}".format(rc))
        # print("error: {}".format(process.stderr.read()))
        return out

#read STDERR


class Todo(Resource):
    def get(self, todo_id):
        print("debug: getting task with the id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def put(self, todo_id):
        print("debug: deleting the task with the id '{}'".format(todo_id))
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

    def delete(self, todo_id):
        print("debug: deleting task with the id '{}'".format(todo_id))
        #abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204





## actually setting up the Api resource routing here
api.add_resource(TodoList, '/todos')

api.add_resource(Todo, '/todos/<todo_id>')

api.add_resource(Ping, '/ping/<ip>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
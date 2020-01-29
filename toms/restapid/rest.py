from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api
from subprocess import Popen

app = Flask(__name__)
api = Api(app)


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


class Todo(Resource):
    def get(self, todo_id):
        #abort_id_code_doesnt_exist(code_id)
        return TODOS[todo_id]
    def delete(self, todo_id):
        print("debug: deleting task with id {}".format(todo_id))
        del TODOS[todo_id]
        return '', 201
    
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id]=task
        return task, 201

class Ping(Resource):
    def get(self, ip):
        print ("debug: pinging adress with url {}".format(ip))
        process = Popen(" ".join['ping', ip, '-c', '1'],
                        stdin = True, stdout = PIPE, stderr = PIPE)
        out = process.stdout_read()
        print("stdout: {}".format(out))
        rc = process.wait()
        print("exit code: {}".format(rc))
        return out

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'copy'},
    'todo3': {'task': 'read'},
    'todo4': {'task': '?????'}
}

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

api.add_resource(TodoList, '/todos')

api.add_resource(Todo, '/todos/todo_id')


# must be at the end
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

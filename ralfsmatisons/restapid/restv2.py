from flask import Flask, request
from flask_restful import reqparse,abort,Resource, Api
#todolist
#shows a list of all todos
class TodoList(Resource):
    def get(self):
        print("debug: sending full list")
        return todos


    def post(self):
        args = parser.parse_args()
        todo_id=int(max(todos.keys()).lstrip("todo")) + 1
        todo_id= "todo%i" % todo_id
        todos[todo_id] = {"task": args["task"]}
        print("debug: added task with it {}".format(todo_id))
        return todos[todo_id], 201
todos = {
    "todo1": {"task": "build an API"},
    "todo2" : {"task" : "?????"},
    }

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

class TodoSimple(Resource):
    def get(self,todo_id):
        return {todo_id: todos[todo_id]}
    

    def put(self,todo_id):
        todos[todo_id] = request.form["data"]
        return {todo_id: todos[todo_id]}

    

    
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
    app.run(debug=True)

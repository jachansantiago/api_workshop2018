from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


todo_list = ["ir al cine", "tarea de algoritmos", "databases"]


@app.route('/', methods=['GET'])
def print_todos():
    return render_template("home.html", todos=enumerate(todo_list))


@app.route('/add', methods=['POST'])
def add_todo():

    # Extract todo from the POST request
    new_todo = request.form["todo"]

    # If the new todo is not empty
    if new_todo:
        # add it to the todo list
        todo_list.append(new_todo)

    # Redirect to HOME
    return print_todos()


@app.route('/delete', methods=['POST'])
def del_todo():

    # Extract todo index from the POST request
    todo_idx = request.form["todo_idx"]
    todo_idx = int(todo_idx) - 1

    # If the todo index is valid
    if todo_idx < len(todo_list) and todo_idx >= 0:
        # delete it from the todo list
        todo_list.pop(todo_idx)

    # Redirect to HOME
    return print_todos()

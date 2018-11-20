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
    # If the new todo is not empty
    # add it to the todo list

    # Redirect to HOME
    return print_todos()


@app.route('/delete', methods=['POST'])
def del_todo():

    # Extract todo index from the POST request
    # If the todo index is valid
    # delete it from the todo list

    # Redirect to HOME
    return print_todos()

from flask import render_template

from app import app
from models.todo_list import tasks

@app.route('/')
def index():
    # return "Hello World!"
    return """<a href="/tasks">/tasks</a>"""

@app.route('/tasks')
def tasks_list():
    return render_template("index.html", title='Home',
        tasks=tasks)

# @app.route('/tasks/<id>')
# def tasks_view_one(id):
#     pass

# @app.route('/tasks', methods=['POST'])
# def tasks_create():
#     pass

# @app.route('/tasks/<id>', methods=['PUT'])
# def tasks_update():
#     pass

# @app.route('/tasks/<id>', methods=['DELETE'])
# def tasks_delete():
#     pass

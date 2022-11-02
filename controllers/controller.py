from flask import Blueprint, render_template

#from app import app
from models.todo_list import tasks

# All about blueprints!
# https://flask.palletsprojects.com/en/2.2.x/blueprints/

blueprint = Blueprint('flask_models', __name__)

@blueprint.route('/')
def index():
    # return "Hello World!"
    return """<a href="/tasks">/tasks</a>"""

@blueprint.route('/tasks')
def tasks_list():
    return render_template("index.html.j2", title='Home',
        tasks=tasks)

# @blueprint.route('/tasks/<id>')
# def tasks_view_one(id):
#     pass

# @blueprint.route('/tasks', methods=['POST'])
# def tasks_create():
#     pass

# @blueprint.route('/tasks/<id>', methods=['PUT'])
# def tasks_update():
#     pass

# @blueprint.route('/tasks/<id>', methods=['DELETE'])
# def tasks_delete():
#     pass

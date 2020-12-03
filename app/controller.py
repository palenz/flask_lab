from flask import render_template, request
from app import app
from app.models.event_list import *
from app.models.event import Event

# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', tasks=tasks)

@app.route('/')
def index():
    return render_template('index.html', title='Test')

# @app.route('/add-task', methods=['POST'])
# def add_tasks():
#     task_title = request.form['title']
#     task_desc = request.form['description']
#     new_task = Task(task_title, task_desc, False)
#     add_new_task(new_task)
#     return render_template('index.html', title='Home', tasks=tasks)
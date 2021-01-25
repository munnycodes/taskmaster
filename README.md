# Task Master
This is a basic task management app called “Task Master”. Users can add tasks to Task Master, the date the task was added is generated automatically. Users are able to add extra tasks, delete completed tasks or update the information about existing tasks. When the task list is empty, users are prompted to add any new tasks they may have to the database.  

## Table of Contents
* [Setup](#setup)
* [Files](#files)
    * [App.py](#app)
    * [Index.html](#index)
    * [style.css](#style.css)


For this project, ensure that you have `python3`, `pip3` and `virtualenv` library set up. 

# Setup
1. Clone this repo onto your local machine.
2. From the root directory, create a virtualenv with the command:
    `python3 -m venv <name of your env>`
3. Activate your virtual env by entering the following command:
    `source <env>/bin/activate`
3. Install requirements:
    `pip install -r requirements.txt`
4. Run the app using the commands:
    `$ export FLASK_APP=app.py`
    `$ flask run`
5. In your browser enter the following URL:
    `http://127.0.0.1:5000/`







# Files

**app.py** contains the functions and routes for creating updating and deleting tasks. 

`App.config` Tells the app where the database is located. 

`db = SQLAlchemy(app)` Initialises the database with settings from the app.  

`Class Todo(db.Model):`  This database model is made up of 3 columns:
	 The `id` column is the automatically generated unique identifier of each entry. 
	 The `content` column is where the actual task is stored as a string. The maximum length of the string is 200 characters (this can be edited by replacing the number in the bracket following `db.string(x)`. `Nullable=False` is set so that the user cannot add an empty task. 
	The `date_created` column uses the `datetime` module to automatically generate a date whenever a task is added. 

@app.route(‘/’) accepts two methods. `[‘POST’] allows the user to post to this route and send data to the database. The if/else statement will add a post(‘content’) to the database if the request is “POST”, otherwise it will just display existing tasks. 

The routes for ‘delete’ and ‘update’ handle the code that removes and modifies entries to the database. 

**index.html** contains the table and form that are presented to the user in the index route. 

**static/style.css** the style definitions are saved here. If you want to change the look of the website you can edit this file.


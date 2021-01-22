from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #locationofdatabase
db= SQLAlchemy(app) #database initiailsed with settings from app

class Todo(db.model):  # create a class +add columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.string(200), nullable=False) #200 = character limit in string, nullable=false so the user can't leave content of task empty.
    date_created = db.Column(db.DateTime, default=datetime.utcnow) #whenever a new task is created, the date and time are created automatically from the imported package datetime 


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
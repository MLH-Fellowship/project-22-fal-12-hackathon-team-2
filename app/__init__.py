import os
from time import time
from flask import Flask, make_response, render_template, request
from dotenv import load_dotenv
from jinja2 import Undefined
from peewee import *
import json
import datetime
from playhouse.shortcuts import model_to_dict
from pymysql import Time
from validator_collection import checkers

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
      user=os.getenv("MYSQL_USER"),
      password=os.getenv("MYSQL_PASSWORD"),
      host=os.getenv("MYSQL_HOST"),
      port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/api/timeline_post', methods=['POST'])
def post_time_post():
    # validate name
    if ('name' in request.form):
        name = request.form['name']
        if (name == ""):
            errorResponse = make_response("Invalid name", 400)
            return errorResponse
    else:
        errorResponse = make_response("Invalid name", 400)
        return errorResponse
    # validate email
    if ('email' in request.form):
        email = request.form['email']
        if (checkers.is_email(email) == False):
            errorResponse = make_response("Invalid email", 400)
            return errorResponse
    else:
        errorResponse = make_response("Invalid email", 400)
        return errorResponse
    # validate content
    if ('content' in request.form):
        content = request.form['content']
        if (content == ""):
            errorResponse = make_response("Invalid content", 400)
            return errorResponse
    else:
        errorResponse = make_response("Invalid name", 400)
        return errorResponse
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    timeline_post_dic = model_to_dict(timeline_post)
    return timeline_post_dic

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/yelp')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/home')
def base():
    return render_template('base.html')

@app.route('/home/<username>')
def about(username):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    if username == "PaulinAlcoser":
        json_url = os.path.join(SITE_ROOT, "static/data", "Paulin.json")
        data = json.load(open(json_url))
        return render_template('about.html', data=data)
    elif username == "AlexisGray":
        json_url = os.path.join(SITE_ROOT, "static/data", "alexis.json")
        data = json.load(open(json_url))
        return render_template('about.html', data=data)
    else:
        return "<h1>Username did not match</h1>"

import os
from webbrowser import get
from flask import Flask, render_template, json, request
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from peewee import *
import datetime
from flask_cors import CORS, cross_origin


load_dotenv()
app = Flask(__name__)
CORS(app)


if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared',
    uri=True)
else:
    print(os.getenv("MYSQL_DATABASE"))
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
        

mydb.connect()
mydb.create_tables([TimelinePost])   


# @app.route('/')
# def index():
#     return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/<username>')
def about(username):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # if username == "PaulinAlcoser":
    #     json_url = os.path.join(SITE_ROOT, "static/data", "Paulin.json")
    #     data = json.load(open(json_url))
    #     return render_template('about.html', data=data)
    # elif username == "AlexisGray":
    #     json_url = os.path.join(SITE_ROOT, "static/data", "alexis.json")
    #     data = json.load(open(json_url))
    #     return render_template('about.html', data=data)
    # else: 
    #     return "<h1>Username did not match</h1>"
    # data_url = username +'1' + ".json"
    
    json_url = os.path.join(SITE_ROOT, "static/data", username + ".json")
    fileExist = os.path.exists(json_url)
    if fileExist:
        data = json.load(open(json_url))
        return render_template('about.html', data=data)
    else: 
        return "<h1>Username did not match</h1>"
    


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get("name", None)
    email = request.form.get("email", None)
    content = request.form.get("content", None)
    if not name:
        return "Invalid name", 400
    if not email or '@' not in email:
        return "Invalid email", 400
    if not content:
        return "Invalid content", 400
    timeline_post = TimelinePost.create(
        name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.asc())
        ]
    }


@app.route('/<username>/timeline')
def timeline(username):
    print(os.getenv("URL"))
    return render_template('timeline.html', data=get_time_line_post(), url=os.getenv("URL")) #delete get_timelin....


# for dirName, subdirList, fileList in os.walk(rootDir , topdown=False):
#     if dirName.endswith("1eb95ebb-d87d-4aac-XX-XX182"):
#         abs_path = os.path.join(dirName, file)
#         print('Found directory: %s' % dirName)
#         #print(fileList)
#         for file in fileList:
#             if file.endswith("activities.json"):
#                 #print('\t%s' % file)
#                 json_data = json.loads(open(abs_path).read())
#                 pprint(json_data)
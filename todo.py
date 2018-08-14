from flask import Flask, render_template,request,redirect,url_for,jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME']='todoflask'
app.config['MONGO_URI']='mongodb://yousufsiddiqui:panacloud123@ds119702.mlab.com:19702/todoflask'
mongo = PyMongo(app)

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/',methods=['POST'])
def add():
        task = mongo.db.task
        task.insert({'task': request.form['task-input']})
        return render_template("success.html")

@app.route('/display')
def display():
        task = mongo.db.task
        list = task.find()
        return render_template('index.html',task=list)


app.run(debug=True)
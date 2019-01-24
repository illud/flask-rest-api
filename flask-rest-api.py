#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask, jsonify
from pymongo import MongoClient
import pprint
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['users']
collection = db['users']

pprint.pprint(collection.find_one())

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/main")
def main():
    return jsonify({'tasks': tasks})
 
if __name__ == "__main__":
    app.run()
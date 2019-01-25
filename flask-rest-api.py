#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#https://ernestocrespo13.wordpress.com/2016/09/27/consulta-a-mongodb-desde-flask-parte-1/
#http://blog.crespo.org.ve/2016/09/crud-usando-flask-y-mongodb-con-orm.html
#https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
from flask import Flask, jsonify, request
from pymongo import MongoClient
import pprint
from bson.json_util import dumps
from bson.objectid import ObjectId

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

#jsonify({'tasks': tasks})

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/main",methods=['GET'])
def main():
    resultados = collection.find({})
    return dumps(resultados)
 
@app.route("/insert", methods=['POST'])
def imse():
    data = {"user": "dragon", "password": "satan"}
    collection.insert_one(request.json)
    return "Inserted"

@app.route("/del", methods=["POST"])
def dell():
    content = request.json
    print (content['_id'])
    collection.delete_one({"_id": ObjectId(content['_id'])})
    return "Deleted"

if __name__ == "__main__":
    app.run(debug= True)

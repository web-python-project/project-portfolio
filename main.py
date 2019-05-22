from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import pymongo
from datetime import timedelta
import json

with open("mongoDB.json") as Json:
    user_doc = json.loads(Json.read())

mongo_url = 'mongodb+srv://'+ user_doc["MongoID"] + ':'+ user_doc['MongoPassword'] + user_doc["MongoURL"]
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')

app = Flask(__name__)
app.secret_key = "111"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



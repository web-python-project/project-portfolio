from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import pymongo

from view.commentAPI import commentAPI
from view.userAPI import userAPI
from view.adminAPI import adminAPI
from view.projectAPI import projAPI

app = Flask(__name__)
#app.register_blueprint(commentAPI)
app.register_blueprint(userAPI)
app.register_blueprint(adminAPI)
app.register_blueprint(projAPI)
app.secret_key = "111"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

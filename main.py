from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import pymongo

from view.API import commonAPI

app = Flask(__name__)
app.register_blueprint(commonAPI)
app.secret_key = "111"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

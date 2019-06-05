from flask import Blueprint, flash, session, render_template, jsonify, request, redirect, url_for

from .db import mongo_connection, projectDAO

import time



db_connection = mongo_connection.ConnectDB().db

posts = postsDAO.Posts(db_connection)



postAPI = Blueprint('postAPI', __name__, template_folder='templates')



def dict_merge(x,y):

	return {**x,**y}



@postAPI.route("/post", methods=["GET", "POST"])

def post():

	if request.method == "GET":

		if "userEmail" in session:

			all_posts = posts.getAllposts()

			return render_template("post.html",info=session["userEmail"], posts=all_posts)

		else:

			flash('You have to logged in')

			return redirect(url_for('userAPI.signin'))



	if request.method == "POST":

		if "userEmail" in session:

			now = time.strftime("%Y-%m-%d %H:%M")

			obj_id = posts.postCreate(dict_merge({"postAuthor":session["userEmail"],"postDate":now},request.form.to_dict(flat=True)))

			all_posts = posts.getAllposts()

			return redirect(url_for('adminAPI.home'))

		else:

			flash('You have to logged in')

			return redirect(url_for('userAPI.signin'))



@postAPI.route("/post/update", methods=["POST"])

def postUpdate():

	if "userEmail" in session:

		print(request.form.to_dict(flat=True)["obj_id"])

		posts.postUpdate(request.form.to_dict(flat=True))

		return redirect(url_for('adminAPI.home'))

	else:

		flash('You have to logged in')

		return redirect(url_for('userAPI.signin'))



@postAPI.route("/post/remove", methods=["POST"])

def postRemove():

	if "userEmail" in session:

		posts.postDelete(request.form.to_dict(flat=True)["obj_id"])

		return redirect(url_for('postAPI.post'))

	else:

		flash('You have to logged in')

		return redirect(url_for('userAPI.signin'))


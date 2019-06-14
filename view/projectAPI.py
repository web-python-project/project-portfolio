from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import mongo_connection, projectDAO, commentDAO

db_connection = mongo_connection.ConnectDB().db

proj0 = projectDAO.Project(db_connection)
comm0 = commentDAO.Comment(db_connection)

projAPI =  Blueprint('projAPI',__name__, template_folder='templates')

@projAPI.route('/detailed', methods=['GET', 'POST'])
def projDetailed():
    if request.method == 'POST':
        index = request.form["_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
    return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm)

@projAPI.route('/postproj', methods=['GET', 'POST'])
def postproj():
    if request.method == 'POST':
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm)

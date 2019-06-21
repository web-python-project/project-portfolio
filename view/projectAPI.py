from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import mongo_connection, projectDAO, commentDAO, adminDAO
import time


db_connection = mongo_connection.ConnectDB().db

admin0 = adminDAO.Admin(db_connection)
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

@projAPI.route('/postComm', methods=['GET', 'POST'])
def postComm():
    if request.method == 'POST':

        #내용공백/비밀번호 기입안했을 때 팝업창 띄우게 해야할듯..
        #내용이 공백이 아니면 댓글 Create
        if request.form["contents"] != "":
            #request.form["date"] = time.strftime("%Y-%m-%d %H:%M")
            comm0.commentCreate(request.form.to_dict(flat='true'))
    
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm)

@projAPI.route('/likeComm', methods=['GET', 'POST'])
def likeComm():
    if request.method == 'POST':
        
        #좋아요 통신
        result = comm0.likeComments(request.form["_id"])
        
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm,index =result)

@projAPI.route('/deleteComm', methods=['GET', 'POST'])
def deleteComm():
    if request.method == 'POST':
        #삭제 통신
        if comm0.deleteComments(request.form.to_dict(flat='true')):
            res = comm0.deleteComments(request.form.to_dict(flat='true'))
        else :
            res = comm0.deleteComments(request.form.to_dict(flat='true'))

        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm, index=res)

@projAPI.route('/deleteProj', methods=['GET', 'POST'])
def deleteProj():
    if request.method == 'POST':
        #삭제 통신
        if proj0.deleteProject(request.form.to_dict(flat='true')):
            res = proj0.deleteProject(request.form.to_dict(flat='true'))
        else :
            res = proj0.deleteProject(request.form.to_dict(flat='true'))
    
        result = admin0.getAdminInfo()
        result_pj = proj0.getAllProject()
        return render_template('home.html',adminInfo=result, projInfo=result_pj)

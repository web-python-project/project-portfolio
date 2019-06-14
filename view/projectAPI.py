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

@projAPI.route('/postComm', methods=['GET', 'POST'])
def postComm():
    if request.method == 'POST':

        #내용이 공백이 아니면 댓글 Create
        if request.form["contents"] != "":
            comm0.commentCreate(request.form.to_dict(flat='true'))
    
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm)

@projAPI.route('/likeComm', methods=['GET', 'POST'])
def likeComm():
    if request.method == 'POST':
        
        #좋아요 통신
        comm0.likeComments(request.form["_id"])
        
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm)

@projAPI.route('/deleteComm', methods=['GET', 'POST'])
def deleteComm():
    if request.method == 'POST':
        
        #삭제 통신
        ###########로그인 기능 추가하기
        res = comm0.deleteComments(request.form["_id"])
        
        index = request.form["proj_id"]
        result_pj = proj0.getOneProject(index)
        result_comm = comm0.getAllComments(index)
        return render_template('detailed.html',projInfo=result_pj, commentInfo =result_comm,index=res)

from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import  mongo_connection, commentDAO

db_connection = mongo_connection.ConnectDB().db

comm0 = commentDAO.Comment(db_connection)

commentAPI =  Blueprint('commentAPI',__name__, template_folder='templates')

#@commentAPI.route('/postproj', methods=['GET', 'POST'])
#def postproj():
#    if request.method == 'POST':
#        return redirect(url_for('projAPI.'))

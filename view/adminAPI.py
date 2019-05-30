from flask import Blueprint,request, render_template, session, redirect, url_for
from .db import adminDAO, mongo_connection

db_connection = mongo_connection.ConnectDB().db
admin0 = adminDAO.Admin(db_connection)

adminAPI =  Blueprint('adminAPI',__name__, template_folder='templates')

@adminAPI.route('/adminsignin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        if not 'adminEmail' in session:
            return render_template('signin.html')
        return render_template('welcome.html', info="관리자 계정으로 로그인 된 상태입니다.")
    elif request.method == 'POST':
        if not 'adminEmail' in session:
            session['adminEmail'] = request.form['adminEmail']
            admin0.adminAuthentication(request.form.to_dict(flat='true'))
            return render_template('welcome.html', info=session['adminEmail'] )
        return render_template('welcome.html', info="관리자 계정으로 로그인 된 상태입니다.")
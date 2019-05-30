from flask import Blueprint,request, render_template, session, redirect, url_for

commonAPI =  Blueprint('bookAPI',__name__, template_folder='templates')

#@commonAPI.route('/home')
#def home():
#    return render_template('home.html')

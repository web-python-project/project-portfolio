from flask import Blueprint,request, render_template, session, redirect, url_for

commentAPI =  Blueprint('commentAPI',__name__, template_folder='templates')

@commentAPI.route('')
def home():
    return render_template('')

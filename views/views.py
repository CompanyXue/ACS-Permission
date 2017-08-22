#!/usr/bin/env python
import sys
sys.path.append("..")
from database.config_setting import app
from business.user_business import UserBusiness
from flask import abort

@app.route('/')
def index():
    return '<h1> Hello World! </h1>'

@app.route('/user/<id>')
def get_user(id):
    xxx = UserBusiness()
    user = xxx.find_user_by_id(id)
    roles = ''
    for i in user.roles:
        print str(i)
        roles += str(i)
        roles += '\t'
    
    if not user:
        abort(404)
    return  '<h1> Hello,%s </h1><h1>Role:  Group</h1>' % user.name + roles




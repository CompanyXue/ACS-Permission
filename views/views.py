#!/usr/bin/env python

from database.models import app
from services.user_service import UserService
from flask import abort

@app.route('/')
def index():
    return '<h1> Hello World! </h1>'

@app.route('/user/<id>')
def get_user(id):
    xxx = UserService()
    user = xxx.find_user_by_id(id)
    roles = ''
    for i in user.roles:
        print str(i)
        roles += str(i)
        roles += '\t'
    
    if not user:
        abort(404)
    return  '<h1> Hello,%s </h1><h1>Role:  Group</h1>' % user.name + roles




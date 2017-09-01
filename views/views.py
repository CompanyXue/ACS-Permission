# -*- coding: UTF-8 -*-
import sys
from flask import abort, request, jsonify, g, url_for, redirect

sys.path.append("..")
from database.config_setting import app
from business.user_business import UserBusiness
from services.user_service import UserService


@app.route('/')
def index():
    return '<h1> Hello World! </h1>'


@app.route('/api/users', methods=['GET'])
def users_manage():
    users = UserBusiness.find_all_users()
    names = ''
    for i in users:
        if i is not None:
            names += i.name + '</br>'
    return '<h1> Users Manage! </h1> </br> %s' % names


@app.route('/api/roles', methods=['GET'])
def roles_manage():
    return '<h1> Roles Manage! </h1>'


@app.route('/user/<int:id>')
def get_user(id):
    user = UserBusiness.find_user_by_id(id)
    roles = ''
    for i in user.roles:
        print(str(i))
        roles += str(i)
        roles += '\t'
    
    if not user:
        abort(404)
    # return '<h1> Hello,%s </h1><h1>Role:  Group</h1>' % user.name + roles
    return jsonify(
        {'username': user.name, 'phone': user.phone, 'email': user.email,
         'created_date': str(user.create_time)})


@app.route('/api/users/create', methods=['POST'])
def new_user():
    data = request.json
    print(data)
    user = UserService.user_add(data)
    print(user.id)
    return (jsonify({'username': user.name, 'phone': user.phone, 'email':
                     user.email, 'created_date': str(user.create_time)}), 201,
            {'Location': url_for('get_user', id=user.id, _external=True)})
    
    
@app.route('/api/users/delete', methods=['POST'])
def delete_user():
    name = request.json.get('username')
    # phone = request.json.get('phone')
    user = UserService.user_delete(name)
    return jsonify(
        {'username': user.name, 'phone': user.phone, 'email': user.email})

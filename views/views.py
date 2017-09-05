# -*- coding: UTF-8 -*-

from flask import abort, request, jsonify, g, url_for, redirect
from flask_jwt import JWT, current_identity
from flask_jwt_extended import (create_access_token, JWTManager, jwt_required,
                                get_jwt_identity, jwt_refresh_token_required,
                                create_refresh_token, get_raw_jwt)

from database.config_setting import app
from business.user_business import UserBusiness
from services.user_service import UserService
from views import utility

jwt = JWTManager(app)
JWT_AUTH_URL_RULE = '/login'


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    print(username)
    password = request.json.get('password', None)
    org = request.json.get('organization', None)
    # first verify user in database
    if username in {u.name: u for u in UserBusiness.find_all_users()}:
        # then verify the user password
        if UserBusiness.verify_password(org, username, password):
            #  user = UserBusiness.find_user_by_name(username)
            ret = {'access_token': create_access_token(username, fresh=True),
                   'refresh_token': create_refresh_token(identity=username)
                   }
            return jsonify(ret), 200
        return jsonify({"msg": "Bad password"}), 401
    return jsonify({"msg": "Username is not exists!"}), 401


# This will generate a new access token from
# the refresh token, but will mark that access token as non-fresh
@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user.name, fresh=False)
    ret = {
        'access_token': new_token
    }
    return jsonify(ret), 200


@app.route('/protected')
@jwt_required
def protected():
    # claims = get_jwt_claims()
    # return '%s' % current_identity
    current_user = get_jwt_identity()
    return jsonify({'hello_from': current_user}), 200


# Endpoint for revoking the current users access token
@app.route('/logout', methods=['DELETE'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    # blacklist.add(jti)
    resp = jsonify({'logout': True})
    # unset_jwt_cookies(resp)
    return jsonify({"msg": "Successfully logged out"}), 200


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
@jwt_required
def get_user(id):
    """
    :获取用户信息
    :param id: 用户id
    :return: json
    """
    user = UserBusiness.find_user_by_id(id)
    roles = []
    for i in user.roles:
        print(str(i))
        # roles += str(i)
        roles.append(i.name)
        
    group = []
    for j in user.group:
        group.append(j.name)
    
    if not user:
        abort(404)
    # return '<h1> Hello,%s </h1><h1>Role:  Group</h1>' % user.name + roles
    return jsonify(
        {'username': user.name, 'phone': user.phone, 'email': user.email,
         'created_date': str(user.create_time), 'roles': roles, 'group': group})


@app.route('/register', methods=['POST'])
def new_user():
    data = request.json
    print(data)
    user = UserService.user_add(data)
    if type(user) == str:
        return jsonify(utility.false_return(data, user)), 402
    if user.id:
        user_obj = {
                    'username': user.name, 'id': user.id, 'email': user.email,
                    'phone': user.phone, 'created_date': str(user.create_time)
        }
        return (jsonify(utility.true_return(user_obj, '用户注册成功！')), 201,
                {'Location': url_for('get_user', id=user.id, _external=True)})


@app.route('/api/users/delete', methods=['POST'])
def delete_user():
    name = request.json.get('username')
    org = request.json.get('organization')
    user = UserService.user_delete(name, org)
    return jsonify(
        {'username': user.name, 'phone': user.phone, 'email': user.email})


@app.route('/api/roles/create', methods=['POST'])
def role_add():
    return '<h1> Roles Manage! </h1>'

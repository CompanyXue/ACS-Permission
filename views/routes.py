# -*- coding: UTF-8 -*-

from database.config_setting import app, date_time
from flask import abort, request, jsonify, url_for, redirect, make_response
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token,  jwt_refresh_token_required, \
    create_refresh_token, get_jwt_identity, set_access_cookies, \
    set_refresh_cookies, unset_jwt_cookies
from views import utility

from business.user_business import UserBusiness
from services.user_service import UserService
from services.role_service import RoleService
from services.permission_service import PermissionService

jwt = JWTManager(app)
# JWT_AUTH_URL_RULE = '/auth/login'


@app.route('/auth/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    print(username)
    password = request.json.get('password', None)
    org = request.json.get('organization', None)
    # first verify user in database
    
    if username not in {u.name: u for u in UserBusiness.find_all_users()}:
        return jsonify({"msg": "Username is not exists!"}), 401
    # then verify the user password
    
    if UserBusiness.verify_password(org, username, password) is False:
        return jsonify({"msg": "Bad password"}), 401
        #  user = UserBusiness.find_user_by_name(username)
    if username != 'mysql' or password != '123456':
        return jsonify({'login': False}), 401
    ret = {'access_token': create_access_token(identity=username),
           'refresh_token': create_refresh_token(identity=username)
           }
    # Create the tokens we will be sending back to the user
    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    # Set the JWT cookies in the response
    resp = jsonify({'login': True})
    
    print(ret['access_token'])
    set_access_cookies(resp, access_token,123456789)
    set_refresh_cookies(resp, refresh_token)
    print("done")
    return jsonify(ret), 200


# This will generate a new access token from
# the refresh token, but will mark that access token as non-fresh
@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    resp = jsonify({
        'refresh': True
    })
    set_access_cookies(resp, new_token)
    return resp, 200


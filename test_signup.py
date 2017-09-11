# -*- coding: UTF-8 -*-

from database.config_setting import app
from flask import abort, request, jsonify, url_for, redirect, make_response
from flask_jwt_extended import JWTManager, jwt_required, \
    create_access_token, jwt_refresh_token_required, \
    create_refresh_token, get_jwt_identity, set_access_cookies, \
    set_refresh_cookies, unset_jwt_cookies
from business.user_business import UserBusiness

jwt = JWTManager(app)


@app.route('/auth/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    print(username)
    password = request.json.get('password', None)
    org = request.json.get('organization', None)
    # first verify user in database
    
    if username in {u.name: u for u in UserBusiness.find_all_users()}:
        return jsonify({"msg": "Username is not exists!"}), 401
    
    # then verify the user password
    if UserBusiness.verify_password(org, username, password):
        #  user = UserBusiness.find_user_by_name(username)
        ret = {'access_token': create_access_token(identity=username),
               'refresh_token': create_refresh_token(identity=username)
               }
        
        # Set the JWT cookies in the response
        resp = jsonify({'login': True})
        
        print(ret['access_token'])
        set_access_cookies(resp, ret['access_token'])
        set_refresh_cookies(resp, ret['refresh_token'])
        print("done")
        
        return jsonify(ret), 200
    return jsonify({"msg": "Bad password"}), 401


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    
    pass

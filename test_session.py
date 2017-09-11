# -*- coding: UTF-8 -*-

from datetime import timedelta
# from database.config_setting import app
from flask import Flask, request, jsonify, session, render_template, redirect
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, \
    create_access_token, jwt_refresh_token_required
import urllib.parse

from business.user_business import UserBusiness
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)
jwt = JWTManager(app)


@app.route('/auth/login')
def login():
    session.permanent = True
    referer = request.args.get('referer', None)
    
    # username = request.json.get('username', None)
    # print(username)
    # password = request.json.get('password', None)
    # org = request.json.get('organization', None)
    #
    # # first verify user in database
    # if username not in {u.name: u for u in UserBusiness.find_all_users()}:
    #     return jsonify({"msg": "Username is not exists!"}), 404
    #
    # if UserBusiness.verify_password(org, username, password) is False:
    #     return jsonify({"msg": "Bad password"}), 403
    
    if referer is not None:
        referer = referer.strip()
    if 'name' in session:
        if referer is not None:
            return redirect(referer + '?ticket=' + 'goal')
    return render_template('login.html', **dict(referer=referer))


@app.route('/dologin')
def doLogin():
    '''这里其实忽略了判断是否登录的流程'''
    session.permanent = True
    referer = request.args.get('referer', None)
    if referer is not None:
        referer = urllib.parse.unquote(referer.strip())

    # 不实现登录功能，直接设置登录态
    session['name'] = 'goal'
    if referer:
        return redirect(referer + '?ticket=' + 'goal')
    else:
        return 'error'
    
    
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
    # set_access_cookies(resp, new_token)
    return resp, 200
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


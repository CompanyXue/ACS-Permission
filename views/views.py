# -*- coding: UTF-8 -*-

from flask import abort, request, jsonify, url_for, redirect, make_response
from flask_jwt_extended import (create_access_token, JWTManager, jwt_required,
                                get_jwt_identity, jwt_refresh_token_required,
                                create_refresh_token, set_refresh_cookies,
                                set_access_cookies, unset_jwt_cookies)
from views import utility
from database.config_setting import app, date_time
from business.user_business import UserBusiness
from services.user_service import UserService
from services.role_service import RoleService
from services.permission_service import PermissionService

jwt = JWTManager(app)
JWT_AUTH_URL_RULE = '/login'


# def require_auth(func):
#     """
#     定义一个装饰器用于装饰需要验证的页面
#     装饰器必须放在route装饰器下面
#     """
#
#     # 定义包装函数
#     def wrapper(*args, **kwargs):
#         try:
#             # 读取cookie
#             user = request.COOKIES['user']
#             opt = request.COOKIES['opt']
#         except:
#             # 出现异常则重定向到登录页面
#             redirect('/login')
#
#         # 验证用户数据
#         if checkShell(user, opt):
#             # 校验成功则返回函数
#             return func(**kwargs)
#         else:
#             # 否则则重定向到登录页面
#             redirect('/login')
#         return wrapper


# 装饰器
def check_login(func):
    def _check_login():
        print(func)
        print(request)
        try:
            print(request.session.get('name', False))
            # 报错name 'request' is not defined，获取不到session
            # return HttpResponseRedirect('/test')
        except KeyError:
            return redirect('/login')  # 跳转至登录页
            # return HttpResponseRedirect('/')
    
    return _check_login


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
            ret = {'access_token': create_access_token(identity=username),
                   'refresh_token': create_refresh_token(identity=username)
                   }
            # Return the double submit values in the resulting JSON
            # instead of in additional cookies
            # resp = jsonify({
            #     'access_csrf' : get_csrf_token(ret['access_token']),
            #     'refresh_csrf': get_csrf_token(ret['refresh_token'])
            # })
            
            # Set the JWT cookies in the response
            resp = jsonify({'login': True})
            
            print(ret['access_token'])
            set_access_cookies(resp, ret['access_token'])
            set_refresh_cookies(resp, ret['refresh_token'])
            print("done")
            return resp, 200
        return jsonify({"msg": "Bad password"}), 403
    return jsonify({"msg": "Username is not exists!"}), 404


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


@app.route('/api/protected', methods=['GET'])
@jwt_required
def protected():
    # claims = get_jwt_claims()
    # return '%s' % current_identity
    current_user = get_jwt_identity()
    return jsonify({'hello_from': '{}'.format(current_user)}), 200


# Endpoint for revoking the current users access token
@app.route('/logout', methods=['POST'])
@jwt_required
def logout():
    # jti = get_raw_jwt()['jti']
    # blacklist.add(jti)
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    
    return resp, 200


@app.route('/api/user/<int:id>')
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


@app.route('/api/users', methods=['GET'])
def users_manage():
    users = UserBusiness.find_all_users()
    names = ''
    for i in users:
        if i is not None:
            names += i.name + '</br>'
    return '<h1> Users Manage! </h1> </br> %s' % names


# update user by id
@app.route('/user/update_user/<_id>', methods=['PUT'])
@check_login
def update_user(_id):
    data = request.get_json()
    update_result = UserService.user_update(_id, data)
    if update_result:
        return jsonify({'message': "success"}), 200
    
    
@app.route('/register', methods=['POST'])
def register_new_user():
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
        # redirect('/login.html'))


@app.route('/api/users/delete', methods=['POST'])
def delete_user():
    name = request.json.get('username')
    org = request.json.get('organization')
    UserService.user_delete(name, org)
    return jsonify(
        {'username': name, 'organization': org, 'modified_date': date_time})


@app.route('/api/roles', methods=['GET'])
def roles_manage():
    return '<h1> Roles Manage! </h1>'


@app.route('/api/roles/create', methods=['POST'])
def role_add():
    data = request.json
    role = RoleService.add_role(data)
    if type(role) == str:
        return jsonify(utility.false_return(data, role)), 402
    if role.id:
        role_obj = {
                    'name': role.name, 'id': role.id, 'type': role.role_type,
                    'created_date': str(role.create_time)
        }
        return jsonify(utility.true_return(role_obj, '角色添加成功！')), 201
    
    
@app.route('/api/roles/delete', methods=['POST'])
def delete_role():
    name = request.json.get('name')
    role_type = request.json.get('type')
    RoleService.delete_role(name)
    return jsonify(
        {'role_name': name, 'role_type': role_type, 'modified_date': date_time})


@app.route('/api/perms/create', methods=['POST'])
def perm_add():
    data = request.json
    perm = PermissionService.add_permission(data)
    if type(perm) == str:
        return jsonify(utility.false_return(data, perm)), 402
    if perm.id:
        perm_obj = {
                    'name': perm.name, 'id': perm.id, 'o_type': perm.o_type,
                    'created_date': str(perm.create_time)
        }
        return jsonify(utility.true_return(perm_obj, '权限添加成功！')), 201
    
    
@app.route('/api/perms/delete', methods=['POST'])
def delete_permission():
    name = request.json.get('name')
    # org = request.json.get('organization')
    PermissionService.delete_permission_by_name(name)
    return jsonify({'permission_name': name, 'modified_date': str(date_time)})


@app.route('/api/users/grant', methods=['POST'])
def grant_user_role():
    user_name = request.json.get('user_name')
    role_name = request.json.get('role_name')
    RoleService.add_user_by_role_name(user_name, role_name)
    return jsonify('用户角色添加成功！'), 201


@app.route('/api/users/grant', methods=['delete'])
def delete_user_role():
    user_name = request.json.get('user_name')
    role_name = request.json.get('role_name')
    RoleService.remove_user_by_role_name(user_name, role_name)
    return jsonify('用户角色移除成功！'), 201



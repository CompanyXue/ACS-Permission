# -*- coding: UTF-8 -*-

from database.models import  User, Role, db

class UserService(object):
    
    def __init__(self, params):
        '''
        Constructor
        '''
# 查询全部用户信息
def find_all_users():
    users = db.session.query(User).all()
    for user in users:
        yield user
    pass
# 根据用户名或者电话号码、组织来查询用户信息
# @return 
def search_user_by_info(name, phone, organization):

    pass
# 根据用户id 查询用户信息
# @return User

def find_user_by_id(userid):
    user = db.session.query(User).filter(User.id==userid).one()
    yield user
    #return user
    pass

# 更新用户信息

def update_user(_id, data):
    pass
##
# （管理员）重置用户密码信息
# @return

def reset_password(username):
    pass
##
 # 修改用户密码
 # @return
 #/
def update_pwd(username,pwd):
    pass
##
 # 根据角色名查询用户数量
 # @return
 #/
def find_count_by_rolename(description):
    pass
##
 # 根据组织id查询全部用户信息
 # @return
 #/
def get_all_by_organization(id):
    pass
##
 # 设置用户所属权限组
 # @return
 #/
def set_user_group(user_group_id):
    pass
def add_users_from_group(users, user_group_id):
    pass
def remove_user_from_group(user_group_id, users):
    pass

# us = UserService.new()
# us.find_all_users()
# us.find_user_by_id(2)      
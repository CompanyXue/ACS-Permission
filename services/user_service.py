# -*- coding: UTF-8 -*-
import hashlib
from database.models import  User, Role, db, Usergroup

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
def search_user_by_info(name, phone):
    users = db.session.query(User).filter(User.name==name|User.phone==phone).all()
    for user in users:
        if user:
            yield user
    pass
# 根据用户id 查询用户信息
# @return User

def find_user_by_id(userid):
    user = db.session.query(User).filter(User.id==userid).one()
    if user is not None:
        # yield user
        return user
    pass

# 更新用户信息

def update_user(_id, data):

    pass

# （管理员）重置用户密码信息
def reset_password(username):
    m = hashlib.md5()
    pwd = m.update('123456')
    user = db.session.query(User).filter(User.name==username).one()
    if user is not None:
        user.pwd = pwd
    pass
##
 # 修改用户密码
 # @return
 #/
def update_pwd(username,pwd):
    user = db.session.query(User).filter(User.name==username).one()
    if user is not None:
        user.pwd = pwd
    pass

# 根据组织id查询全部用户信息
# @return
#/
def get_all_by_organization(id):
    users = db.session.query(User).filter(User.organization==id).all()
    for user in users:
        if user:
            yield user
    pass

def delete_user_by_id(id):
    user = db.session.query(User).filter(User.id==id).one()
    if user is not None:
        print user
        db.session.delete(user)
        # yield user
    pass
        
def delete_user_by_name(name):
    user = db.session.query(User).filter(User.name==name).one()
    if user is not None:
        yield user
        db.session.delete(user)
        
# 设置用户所属权限组
def add_users_into_group(users, user_group):
    for  user in users:
        if user is not None:
            user.add_user_group(user_group)
    pass
 
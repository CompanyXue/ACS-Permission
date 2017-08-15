# -*- coding: UTF-8 -*-

import hashlib
from database.models import  User, Role, db, Usergroup

class UserService(object):

    def __init__(self):
        '''
        Constructor
        '''

    def add_user(self,user):
        pass

    # 查询全部用户信息
    def find_all_users(self):
        users = db.session.query(User).all()
        for user in users:
            yield user
        pass

    # 根据用户名或者电话号码、组织来查询用户信息
    # @return
    def search_user_by_info(self, name, phone):
        users = db.session.query(User).filter_by(name=name, phone=phone).all()
        for user in users:
            if user is not None:
                print '用户'
                yield user
        pass

    # 根据用户id 查询用户信息
    # @return User
    def find_user_by_id(self,userid):
        user = db.session.query(User).filter(User.id==userid).one()
        if user is not None:
            # yield user
            return user
        pass

    # 更新用户信息
    @classmethod
    def update_user(self, data):

        pass

    # 修改用户密码
    # @return
    def update_pwd(self,username,pwd):
        user = db.session.query(User).filter(User.name==username).one()
        if user is not None:
            user.pwd = pwd
        pass

    # （管理员）重置用户密码信息
    @classmethod
    def reset_password(username):
        m = hashlib.md5()
        pwd = m.update('123456')
        user = db.session.query(User).filter(User.name==username).one()
        if user is not None:
            user.pwd = pwd
        pass

    # 根据组织id查询全部用户信息
    # @return
    def get_all_by_organization(self,o_id):
        users = db.session.query(User).filter(User.organization==o_id).all()
        for user in users:
            if user:
                yield user
        pass

    def delete_user_by_id(self,id):
        user = db.session.query(User).filter(User.id==id).first()
        if user is not None:
            print user
            db.session.delete(user)
            print ' 已删除！！'
            # yield user
        pass

    def delete_user_by_name(self,name):
        user = db.session.query(User).filter(User.name==name).one()
        if user is not None:
            yield user
            db.session.delete(user)
        pass
    
    # 设置用户所属权限组
    @classmethod
    def add_users_into_group(users, user_group):
        for  user in users:
            if user is not None:
                user.add_user_group(user_group)
        pass
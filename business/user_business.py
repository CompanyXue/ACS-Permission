# -*- coding: UTF-8 -*-

import hashlib
import sys,time
sys.path.append("..")
# sys.path.insert(0,"..")
from database.config_setting import db
from database.user_db import User
from database.role_db import Role
from database.user_group_db import Usergroup

class UserBusiness(object):
    time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def add_user(self,user):
        if user is not None:
            # if user.name in users.name 
            db.session.add(user)
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
                print ('用户')
                yield user
        pass

    # 根据用户id 查询用户信息
    # @return User
    def find_user_by_id(self,userid):
        user = db.session.query(User).filter(User.id==userid).first()
        if user is not None:
            # yield user
            return user
        pass

    # 更新用户信息
    def update_user(self, id, data):
        user = db.session.query(User).filter(User.id==id).first()
        if user is not None:
            user.name = data['name']
            user.pwd = user['password']
            user.email = user['email']
            user.sex = user['sex']
            user.modified_date = time
            user.modified_by = user['modified_by']
            user.is_deleted = user['is_deleted']
            db.session.commit()
        return user

    # 修改用户密码
    # @return
    def update_pwd(self,username,pwd):
        user = db.session.query(User).filter(User.name==username).first()
        if user is not None:
            user.pwd = pwd
        pass

    # （管理员）重置用户密码信息
    @classmethod
    def reset_password(username):
        m = hashlib.md5()
        pwd = m.update('123456')
        user = db.session.query(User).filter(User.name==username).first()
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
    
    @classmethod
    def delete_user_by_id(self,id):
        user = db.session.query(User).filter(User.id==id).first()
        if user is not None:
            # db.session.delete(user)
            user.is_deleted = True
            yield user
            print ' 已删除！！'
        pass
    
    @classmethod
    def delete_user_by_name(self,name):
        user = db.session.query(User).filter(User.name==name).first()
        if user is not None:
            yield user
            # 此处的删除 并非现实意义的删除，而是将标志is_deleted置为1
            # db.session.delete(user)
            user.is_deleted = True
        pass
    
    # 设置用户所属权限组
    @classmethod
    def add_users_into_group(users, user_group):
        for user in users:
            if user is not None:
                user.add_user_group(user_group)
        pass
    



# -*- coding: UTF-8 -*-

import sys

sys.path.append("..")
# sys.path.insert(0,"..")
from passlib.hash import sha256_crypt

from database.config_setting import db, date_time
from database.user_db import User


class UserBusiness(object):
    def __init__(self):
        '''
        Constructor
        '''

    @classmethod
    def add_user(self, user):
        if user is not None:
            # if user.name in users.name 
            db.session.add(user)
            db.session.commit()
        pass

    # 查询全部用户信息
    @classmethod
    def find_all_users(self):
        users = db.session.query(User).all()
        for user in users:
            yield user
        pass

    # 根据用户名或者电话号码、组织来查询用户信息
    # @return
    @classmethod
    def search_user_by_info(self, name, phone):
        users = User.query().filter_by(name=name, phone=phone).all()
        for user in users:
            if user is not None:
                print('用户')
                yield user
        pass

    # 根据用户id 查询用户信息
    # @return User
    @classmethod
    def find_user_by_id(self, userid):
        user = db.session.query(User).filter(User.id == userid).first()
        if user is not None:
            # yield user
            return user
        pass

    # 更新用户信息
    @classmethod
    def update_user(self, id, data):
        # 如果用 update()，则更新的内容必须是 Dict 数据类型.
        # user = db.session.query(User).update({'name': data.name,'sex':data.sex})
        user = db.session.query(User).filter(User.id == id).first()
        if user is not None:
            user.name = data['name']
            user.pwd = data['password']
            user.email = data['email']
            user.sex = data['sex']
            user.modified_date = date_time
            user.modified_by = user['modified_by']
            user.is_deleted = user['is_deleted']
            db.session.commit()
        return user

    # 修改用户密码
    # @return
    @classmethod
    def update_pwd(self, username, pwd):
        user = User.query().filter(name=username).first()
        if user is not None:
            user.pwd = sha256_crypt.encrypt(pwd)
            user.modified_date = date_time
            db.session.commit()
        pass

    # 根据组织id查询全部用户信息
    # @return
    @classmethod
    def get_all_by_organization(self, o_id):
        users = User.query().filter(organization=o_id).all()
        for user in users:
            if user.is_deleted is False:
                yield user
        pass

    # （管理员）重置用户密码信息
    @classmethod
    def reset_password(username):
        default_pwd = ('123456')
        user = User.query().filter(name=username).first()
        if user is not None:
            user.pwd = sha256_crypt.encrypt(default_pwd)
            user.modified_date = date_time
            db.session.commit()
        pass

    '''
    * 根据用户id禁用某用户，删除掉
    * @return user 
    '''

    @classmethod
    def delete_user_by_id(self, id):
        user = User.query().filter(id=id).first()
        if user is not None:
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            db.session.commit()
            return user
        pass

    # 根据用户名字删除某用户
    # @return user 
    @classmethod
    def delete_user_by_name(self, name):
        user = db.session.query(User).filter(User.name == name).first()
        if user is not None:
            # 此处的删除 并非现实意义的删除，而是将标志is_deleted置为1
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            db.session.commit()
            return user
        pass

    # 设置用户所属用户组
    @classmethod
    def add_user_into_group(self, user_name, user_group):
        user = User.query().filter(name=user_name).first()
        if user is not None:
            user.group.apppend(user_group)
            user.modified_date = date_time
            db.session.commit()

    # 验证用户密码
    @classmethod
    def verify(self, user, password):
        return sha256_crypt.verify(password, user.pwd)

    # 传入参数更新用户可更改内容
    @classmethod
    def update(self, data):
        self.name = data.name
        self.phone = data.phone
        self.email = data.email
        self.modified_date = date_time
        self.organization = data.organization

# -*- coding: UTF-8 -*-
# sys.path.insert(0,"..")

from passlib.hash import sha256_crypt

from database.config_setting import db, date_time
from database.user_db import User


class UserBusiness(object):
    def __init__(self):
        pass

    @classmethod
    def add_user(cls, user):
        if user is not None:
            # if user.name in users.name 
            db.session.add(user)
            db.session.commit()
        pass

    # 查询全部用户信息
    @classmethod
    def find_all_users(cls):
        users = db.session.query(User).all()
        for user in users:
            yield user
        pass

    # 根据用户名或者电话号码、组织来查询用户信息
    # @return
    @classmethod
    def search_user_by_info(cls, name, phone):
        users = User.query().filter_by(name=name, phone=phone).all()
        for user in users:
            if user is not None:
                print('用户')
                yield user
        pass

    # 根据用户id 查询用户信息
    # @return User
    @classmethod
    def find_user_by_id(cls, user_id):
        user = db.session.query(User).filter(User.id == user_id).first()
        if user is not None:
            return user
        pass

    # 根据用户id 查询用户信息
    # @return User
    @classmethod
    def find_user_by_name(cls, user_name):
        user = db.session.query(User).filter(User.name == user_name).first()
        if user is not None:
            return user
        pass

    # 更新用户信息
    @classmethod
    def update_user(cls, name, data):
        # 如果用 update()，则更新的内容必须是 Dict 数据类型.
        # user = db.session.query(User).update({'name': data.name,'sex':data.sex})
        user = cls.find_user_by_name(name)

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
    def update_pwd(cls, username, pwd):
        user = cls.find_user_by_name(username)
        if user is not None:
            user.pwd = sha256_crypt.encrypt(pwd)
            user.modified_date = date_time
            db.session.commit()
        pass

    # 根据组织id查询全部用户信息
    # @return
    @classmethod
    def get_all_by_organization(cls, o_id):
        users = User.query().filter(organization=o_id).all()
        for user in users:
            if user.is_deleted is False:
                yield user
        pass

    # （管理员）重置用户密码信息
    @classmethod
    def reset_password(cls, username):
        default_pwd = '123456'
        user = cls.find_user_by_name(username)
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
    def delete_user_by_id(cls, user_id):
        user = User.query().filter(id=user_id).first()
        if user is not None:
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            db.session.commit()
            return user
        pass

    # 根据用户名字 删除某用户
    # @return user 
    @classmethod
    def delete_user_by_name(cls, name):
        user = cls.find_user_by_name(name)
        if user is not None:
            # 此处的删除 并非现实意义的删除，而是将标志is_deleted置为1
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            db.session.commit()
            return user
        pass

    # 验证用户密码
    @classmethod
    def verify(cls, user_name, password):
        user = cls.find_user_by_name(user_name)
        return sha256_crypt.verify(password, user.pwd)

    # 传入参数更新用户可更改内容
    @classmethod
    def update_user(cls, name, data):
        user = cls.find_user_by_name(name)
        user.name = data.name
        user.phone = data.phone
        user.email = data.email
        user.modified_date = date_time
        user.organization = data.organization
        db.session.commit()

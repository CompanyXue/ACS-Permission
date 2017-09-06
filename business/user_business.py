# -*- coding: UTF-8 -*-
# sys.path.insert(0,"..")

from passlib.hash import sha256_crypt
from sqlalchemy.exc import SQLAlchemyError
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
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return str(e)

    @classmethod
    def create_user(cls, data):
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        phone = data.get('phone')
        organization = data.get('organization', None)
        sex = data.get('sex')
        
        if username is None or password is None or email is None or phone is None:
            return (u"缺失用户-信息参数")  # missing arguments

        user = User(name=username, pwd=password, sex=sex, phone=phone,
                    email=email, organization=organization,
                    create_by='Super User')
        return user
    
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
    def search_user_by_info(cls, name, org):
        user = db.session.query(User).filter_by(name=name, organization=org).first()
        if user is not None:
            return user

    # 根据用户id 查询用户信息
    # @return User
    @classmethod
    def find_user_by_id(cls, user_id):
        user = db.session.query(User).filter(User.id == user_id).first()
        if user is not None:
            return user
        pass

    # 根据用户name 查询用户信息
    # @return User
    @classmethod
    def find_user_by_name(cls, user_name):
        user = db.session.query(User).filter_by(name=user_name).first()
        if user is not None:
            return user
        pass

    # 根据用户name + org 查询用户信息
    # @return User
    @classmethod
    def find_user_by_org_name(cls, org, user_name):
        user = db.session.query(User).filter(User.name == user_name,
                                             User.organization == org).first()
        if user is not None:
            return user
        pass
    
    # 传入参数更新用户可更改内容信息
    @classmethod
    def update_user(cls, id, data):
        # 如果用 update()，则更新的内容必须是 Dict 数据类型.
        # user=db.session.query(User).update({'name': data.name,'sex':data.sex})
        user = cls.find_user_by_id(id)
        if user:
            user.name = data.get('name', None)
            user.phone = data.get('phone')
            user.email = data.get('email')
            user.pwd = sha256_crypt.encrypt(data.get('password'))
            user.organization = data.get('organization')
            user.sex = data.get('sex', None)
            user.status = data.get('status')
            user.modified_date = date_time
            user.modified_by = user.name
            user.is_deleted = False
            db.session.commit()

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

    # 根据组织名称 查询全部用户信息
    # @return
    @classmethod
    def get_all_by_organization(cls, o_name):
        users = db.session.query(User).filter(User.organization == o_name).all()
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
        user = db.session.query(User).filter_by(id=user_id).first()
        if user is not None:
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            user.modified_by = 'Super User'
            db.session.commit()
            return user
        pass

    # 根据用户名字 删除某用户
    # @return user 
    @classmethod
    def delete_user_by_name(cls, name):
        user = cls.find_user_by_name(name)
        if user is not None and user.is_deleted is False:
            # 此处的删除 并非现实意义的删除，而是将标志is_deleted置为1
            # db.session.delete(user)
            user.is_deleted = True
            user.modified_date = date_time
            user.modified_by = 'Super User'
            db.session.commit()
            return user
        pass

    # 验证用户密码
    # @return True-正确 ， False-错误
    @classmethod
    def verify_password(cls, org, user_name, password):
        user = cls.find_user_by_org_name(org, user_name)
        if user:
            return sha256_crypt.verify(password, user.pwd)

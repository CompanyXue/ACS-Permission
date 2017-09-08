# -*- coding: UTF-8 -*-

from sqlalchemy.exc import SQLAlchemyError
from database.role_db import Role
from database.config_setting import db


class RoleBusiness(object):
    def __init__(self):
        pass

    # 查询全部角色信息
    @classmethod
    def find_all_roles(cls):
        roles = db.session.query(Role).all()
        for i in roles:
            yield i
        pass

    # 根据用户角色名查找有哪些用户
    # @param role_name
    # @return
    @classmethod
    def find_by_role_name(cls, role_name):
        role = db.session.query(Role).filter(Role.name == role_name).first()
        if role is not None:
            return role

    # 创建角色对象
    @classmethod
    def create_role(cls, data):
        role_name = data.get('name')
    
        role_type = data.get('type')
    
        if role_name is None or role_type is None:
            return "缺失信息参数"  # missing arguments
    
        role = Role(name=role_name, role_type=role_type, create_by='Super User')
        return role

    # 添加角色进数据库
    @classmethod
    def add_role(cls, role):
        if role is not None:
            db.session.add(role)
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return str(e)

    # 传入参数更新用户可更改内容信息
    @classmethod
    def update_role(cls, name, data):
        
        pass
    
    '''
    * 根据角色id 刪除角色
    * @param role_id
    * @return role
    '''
    @classmethod
    def delete_role_by_id(cls, role_id):
        role = db.session.query(Role).filter(Role.id == role_id).first()
        if role is not None:
            db.session.delete(role)
            db.session.commit()
            print(role + '被删除！')
        pass

    # 添加角色
    def add_user_by_role_name(cls, user, role_name):
        role = cls.find_by_role_name(role_name)
        if role is not None and user is not None:
            role.users.append(user)
            print(role.name + '--添加--' + user.name + '--用户成功！')
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return str(e)

    # 添加角色
    def remove_user_by_role_name(cls, user, role_name):
        role = cls.find_by_role_name(role_name)
        if role is not None and user is not None:
            role.users.remove(user)
            print(role.name + '--移除--' + user.name + '--用户成功！')
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return str(e)
    '''
    * 根据名稱刪除角色
    * @param role_name
    * @return role
    '''
    @classmethod
    def delete_role_by_name(cls, role_name):
        role = cls.find_by_role_name(role_name)
        if role is not None:
            db.session.delete(role)
            db.session.commit()
            print(role + '被删除！')
        pass

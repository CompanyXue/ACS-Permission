# -*- coding: UTF-8 -*-
import sys

sys.path.append("..")

from database.role_db import Role
from database.config_setting import db, date_time


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

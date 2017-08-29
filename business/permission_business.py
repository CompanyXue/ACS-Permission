# -*- coding: UTF-8 -*-
import time
import sys

sys.path.append("..")
# from database.models import Permission,Role,db
from database.config_setting import db, date_time
from database.permission_db import Permission
from database.role_db import Role


class PermissionBusiness(object):
    def __init__(self):
        '''
        Constructor
        '''

    # 查询出所有的权限列表
    # @return perms
    @classmethod
    def find_all_permission(self):
        perms = db.session.query(Permission).all()
        for re in perms:
            if re is not None:
                yield re
        pass

    '''
     * 根据用户角色获取该用户的权限
     * @param role_name
     * @return perms
    '''

    @classmethod
    def find_perm_by_role(self, role_name):
        role = db.session.query(Role).filter(Role.name == role_name).first()
        if role is not None:
            for perm in role.perms:
                if perm is not None:
                    yield perm
        pass

    '''
    * 根据权限名称获取用户角色
    * @param perm_name
    * @return roles
    '''

    @classmethod
    def find_roles_by_perm(self, perm_name):
        perm = db.session.query(Permission).filter(Permission.name == perm_name).first()
        if perm is not None:
            for role in perm.roles:
                if role is not None:
                    yield role
        pass

    '''
    * 根据权限名称获取资源信息
    * @param perm_name
    * @return resources
    '''

    @classmethod
    def find_resource_by_perm(self, perm_name):
        perm = db.session.query(Permission).filter(Permission.name == perm_name).first()
        if perm is not None:
            for i in perm.resources:
                yield i
        pass

    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perms
    '''

    @classmethod
    def add_permission(self, perm1):
        print('添加权限XXX')
        if db.session.query(Permission).filter(Permission.name==perm1.name).first() is None:
            # 去掉重复的name
            db.session.add(perm1)
            db.session.commit()
            print('添加成功')

    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perm
    '''

    @classmethod
    def delete_permission_by_name(self, perm_name):
        perm = db.session.query(Permission).filter(Permission.name == perm_name).first()
        if perm is not None:
            print(perm)
            db.session.delete(perm)
            db.session.commit()
        pass

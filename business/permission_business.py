# -*- coding: UTF-8 -*-
from sqlalchemy.exc import SQLAlchemyError
from database.config_setting import db
from database.permission_db import Permission
from database.role_db import Role


class PermissionBusiness(object):
    def __init__(self):
        """
        Constructor
        """

    # 查询出所有的权限列表
    # @return perms
    @classmethod
    def find_all_permission(cls):
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
    def find_perm_by_role(cls, role_name):
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
    def find_by_name(cls, perm_name):
        perm = db.session.query(Permission).filter_by(name=perm_name).first()
        if perm is not None:
            return perm
        pass

    '''
    * 根据权限名称获取资源信息
    * @param perm_name
    * @return resources
    '''

    @classmethod
    def find_resource_by_perm(cls, perm_name):
        perm = cls.find_by_name(perm_name)

        for i in perm.resources:
            yield i
        pass

    '''
    * 添加用户的权限
    * @param perm_obj
    * @return perms
    '''

    @classmethod
    def add_permission(cls, perm1):
        print('添加权限XXX')
        if cls.find_by_name(perm1.name) is None:
            # 去掉重复的name
            db.session.add(perm1)
            try:
                db.session.commit()
            except SQLAlchemyError as e:
                db.session.rollback()
                return str(e)
            print('添加成功！')
            return perm1
        else:
            return "该权限已存在,请重新输入！"

    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perm
    '''
    @classmethod
    def delete_permission(cls, perm1):
        if perm1 is not None:
            print(perm1)
            db.session.delete(perm1)
            db.session.commit()
            print('删除成功！')
        pass

    # 创建角色对象
    @classmethod
    def create_permission(cls, data):
        perm_name = data.get('name')
        perm_type = data.get('type')
        perm_content = data.get('content', None)
        
        if perm_name is None or perm_type is None or perm_content is None:
            return "缺失信息参数"  # missing arguments

        perm = Permission(name=perm_name, o_type=perm_type,
                          content=perm_content, create_by='Super User')
        return perm

    # 传入参数更新用户可更改内容信息
    @classmethod
    def update_role(cls, name, data):
        
        pass

# -*- coding: UTF-8 -*-
from business.permission_business import Permission, PermissionBusiness
from business.resource_business import ResourceBusiness
from business.role_business import RoleBusiness
from database.config_setting import db, date_time


class PermissionService(object):
    def __init__(self):
        pass

    '''
     * 根据用户角色获取该用户的权限
     * @param role_name
     * @return perm set
    '''
    @classmethod
    def find_perm_by_role(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)
        for perm in role.perms:
            if perm is not None:
                yield perm
        pass

    '''
     * 根据资源获取该用户的权限
     * @param role_name
     * @return perm set
    '''
    @classmethod
    def find_perm_by_resource(cls, res_name):
        res = ResourceBusiness.find_by_name(res_name)
        for perm in res.perms:
            if perm is not None:
                yield perm
        pass

    '''
    * 根据权限名称获取用户角色
    * @param perm_name
    * @return role set
    '''
    @classmethod
    def find_roles_by_perm(cls, perm_name):
        perm = PermissionBusiness.find_by_name(perm_name)
        if perm is not None:
            for role in perm.roles:
                if role is not None:
                    yield role
        pass

    '''
    * 根据权限名字添加用户的权限
    * @param perm_name
    * @return perm
    '''
    @classmethod
    def add_permission_by_name(cls, perm_name):
        print(u'类中的时间: ', date_time)
        perm = Permission(name=str(perm_name), o_type='2', create_by='Admin',
                          content='TODO ')
        PermissionBusiness.add_permission(perm)

    # 通过json创建对象，添加权限
    @classmethod
    def add_permission(cls, data):

        perm = PermissionBusiness.create_permission(data)
        if type(perm) == str:
            return perm

        if RoleBusiness.find_by_role_name(perm.name):
            # if UserBusiness.find_user_by_name(username):
            return "该权限已存在,请重新输入！"
        else:
            PermissionBusiness.add_permission(perm)
            return perm
        
    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perm
    '''
    @classmethod
    def delete_permission_by_name(cls, perm_name):

        perm = PermissionBusiness.find_by_name(perm_name)
        if perm is not None:
            PermissionBusiness.delete_permission(perm)

    '''
    * 根据名稱添加用户的权限
    * @param role_name
    * @return role
    '''

    @classmethod
    def add_permission_by_role_name(cls, perm_name, role_name):
        perm = PermissionBusiness.find_by_name(perm_name)
        role = RoleBusiness.find_by_role_name(role_name)
        if role is not None and perm is not None:
            role.perms.append(perm)
            print(role.name + '--添加--' + perm.name + '--权限成功！')
        db.session.commit()
        pass

    '''
    * 根据名稱移除角色的权限
    * @param role_name,perm_name
    * @return 
    '''

    @classmethod
    def remove_permission_by_name(cls, perm_name, role_name):
        perm = PermissionBusiness.find_by_name(perm_name)
        role = RoleBusiness.find_by_role_name(role_name)
        if role is not None and perm is not None:
            if perm in role.perms:
                role.perms.remove(perm)
                role.modified_date = date_time
            print(role.name + '--移除--' + perm.name + '--权限成功！')
            db.session.commit()

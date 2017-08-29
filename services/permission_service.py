# -*- coding: UTF-8 -*-
from business.permission_business import Permission,PermissionBusiness
from business.role_business import Role
from database.config_setting import date_time, date_now

class PermissionService(object):
    def __init__(self):
        '''
        Constructor
        '''

    # 查询出所有的权限列表
    @classmethod
    def find_all_permission(self):
        perms = Permission.query().all()
        for re in perms:
            if re is not None:
                yield re
        pass

    '''
     * 根据用户角色获取该用户的权限
     * @param role_name
     * @return perm set
    '''

    @classmethod
    def find_perm_by_role(self, role_name):
        role = Role.query().filter(name=role_name).one()
        for perm in role.perms:
            if perm is not None:
                yield perm
        pass

    '''
    * 根据权限名称获取用户角色
    * @param perm_name
    * @return role set
    '''

    @classmethod
    def find_roles_by_perm(self, perm_name):
        perm = Permission.query().filter(name=perm_name).one()
        for role in perm.roles:
            if role is not None:
                yield role
        pass

    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perm
    '''

    @classmethod
    def add_permission_by_name(self, perm_name):
        print(u'类中的时间: ', date_now)
        perm = Permission(name=str(perm_name), o_type='2',create_by='Admin',content='TODO ')
        PermissionBusiness.add_permission(perm)

    '''
    * 根据权限名字刪除用户的权限
    * @param perm_name
    * @return perm
    '''

    @classmethod
    def delete_permission_by_name(self, perm_name):

        perm = Permission.query().filter(name=perm_name).first()
        if perm is not None:
            print (perm)
            Permission.delete(perm)
    pass

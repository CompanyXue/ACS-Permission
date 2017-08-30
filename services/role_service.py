# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness
from business.permission_business import PermissionBusiness


class RoleService(object):
    def __init__(self):
        pass

    '''
    # 根据用户角色名查找有哪些用户
    # @param role_name
    # @return
    '''
    @classmethod
    def find_users_by_role_name(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)

        for user in role.users:
            yield user
        pass

    '''
     * 根据用户的Id查找用户的角色信息
     * @param userId
     * @return
    '''
    @classmethod
    def find_role_by_user_id(cls, user_id):
        user = UserBusiness.find_user_by_id(user_id)
        if user is not None:
            for role in user.roles:
                yield role
        pass

    ''' 
     * 根据用户名查找用户拥有的角色信息
     * @param username
     * @return Set<Role>
    '''
    @classmethod
    def find_role_by_user_name(cls, user_name):
        user = UserBusiness.find_user_by_name(user_name)
        if user is not None:
            for role in user.roles:
                yield role
        pass

    ''' 
     * 根据角色名查找资源信息（权限）
     * @param role_name
     * @return 
    '''
    @classmethod
    def find_resource_by_role_name(cls, role_name):
        perms = PermissionBusiness.find_perm_by_role(role_name)
        for perm in perms:
            for i in perm.resources:
                yield i
        pass

    ''' 
     * 根据角色名查找资源信息（权限）
     * @param role_name
     * @return 
    '''
    @classmethod
    def find_group_by_role_name(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)
        for i in role.group:
            yield i
        users = role.users
        for user in users:
            print(user)
            for j in user.group:
                yield j

    # 通过名称添加角色
    @classmethod
    def add_role_by_name(cls, role_name):

        pass

    # 通过名称删除角色
    @classmethod
    def delete_role(cls, role_name):
        RoleBusiness.delete_role_by_name(role_name)

# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness
from business.user_group_business import UsergroupBusiness


class RoleService(object):
    def __init__(self):
        '''
        Constructor
        '''

    # 根据用户角色名查找有哪些用户
    # @param role_name
    # @return
    @classmethod
    def find_users_by_role_name(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)

        for user in role.users:
            yield user
        pass

    ''' 
    * 根据用户名查找用户拥有的角色信息
    * 根据角色id 刪除角色
    * @param role_id
    * @return role
    '''

    @classmethod
    def add_role_by_name(self, role_name):

        pass

    '''
     * 根据用户的Id查找用户的角色信息
     * @param userId
     * @return
    '''
    @classmethod
    def find_role_by_user_id(cls, user_id):
        user =  UserBusiness.find_user_by_id(user_id)
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
    def find_resource_by_user_name(cls, user_name):
        user = UserBusiness.find_user_by_name(user_name)
        if user is not None:
            for role in user.perms.resources:
                yield role
        pass
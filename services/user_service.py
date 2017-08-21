# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness
from business.user_group_business import UsergroupBusiness

class UserService(object):
    
    ub = UserBusiness()
    rb = RoleBusiness()
    ugb = UsergroupBusiness()

    def __init__(self):
        '''
        Constructor
        '''
    
    def signup(self, request):
        
        pass
    
    def manage(self,user):
        #数据库添加用户
        ub.add(user)
        # 用户添加组
    
        ub.add_users_into_group(user,user_group)
        # 用户添加角色
        # roles = find_all_roles()
        user.roles.append(roles)
        pass
    
    
    
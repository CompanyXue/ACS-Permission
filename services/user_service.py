# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness

class UserService(object):
    
    aa = UserBusiness()

    def __init__(self):
        '''
        Constructor
        '''
        
    def signup(self,user):
        #数据库添加用户
        aa.add(user)
        # 用户添加组

        aa.add_users_into_group(user,user_group)
        # 用户添加角色
        
        pass
    

# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
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
    
    def user_query(username=None, phone=None):
        user = ub.search_user_by_info(username, phone)
        _id = str(user['_id'])
        organization = str(user['organization'])
        groups = user['groups']
        for i in range(0, len(groups)):
            groups[i] = str(groups[i])
        groups = ugb.form_group_object(groups)
        
        
        print (user)
        name = user['name']
        pwd = user['password']
        email = user['email']
        sex = user['sex']
        is_deleted = user['is_deleted']
        
        if phone is None:
            phone = user['phone']
        if username is None:
            username = user['email']
        user_obj = User(name, phone, organization,
                    groups, group_id, name, mail, is_activated, is_worker, pwd, _id)
        return user_obj
        pass
    def request(self, request):
        user = request.object
        
        pass
    
    def manage(self,user,user_group,role):
        #数据库添加用户
        ub.add(user)
        # 用户添加组
        if user_group is not None:
            ub.add_users_into_group(user,user_group)
        # 用户添加角色
        # roles = find_all_roles()
        user.roles.append(roles)
        pass
    
    
    
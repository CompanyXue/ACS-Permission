# -*- coding: UTF-8 -*-
from database.config_setting import db, date_time
from business.user_business import UserBusiness
from business.user_group_business import UsergroupBusiness


class UserGroupService(object):
    def __init__(self):
        '''
        Constructor
        '''

    # 设置用户所属用户组
    @classmethod
    def add_user_into_group(cls, user_name, group_name):
        user = UserBusiness.find_user_by_name(user_name)
        user_group = UsergroupBusiness.find_group_by_name(group_name)

        user.group.append(user_group)
        user.modified_date = date_time
        print (user.name + "--添加到用户组--" + user_group.name + '--成功！')
        db.session.commit()

    # 删除用户所属用户组
    @classmethod
    def remove_user_from_group(cls, user_name, group_name):
        user = UserBusiness.find_user_by_name(user_name)
        user_group = UsergroupBusiness.find_group_by_name(group_name)

        user.group.remove(user_group)
        user.modified_date = date_time
        print(user.name + "-从用户组-" + user_group.name + '-移除成功！')
        db.session.commit()

    '''
    * 根据用户组名查找有哪些用户
    * @param role_name
    * @return 
    '''
    @classmethod
    def find_users_by_group_name(self, group_name):
        group = UsergroupBusiness.find_group_by_name(group_name)

        for user in group.users:
            if user is not None:
                yield user
        pass
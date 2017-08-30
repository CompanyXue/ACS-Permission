# -*- coding: UTF-8 -*-
from database.config_setting import db, date_time
from business.user_business import UserBusiness
from business.user_group_business import UsergroupBusiness


class UserGroupService(object):
    def __init__(self):
        pass

    # 设置用户所属用户组
    @classmethod
    def add_user_into_group(cls, user_name, group_name):
        user = UserBusiness.find_user_by_name(user_name)
        user_group = UsergroupBusiness.find_group_by_name(group_name)

        user.group.append(user_group)
        user.modified_date = date_time
        print (user.name + "--添加到用户组--" + user_group.name + '--成功！')
        db.session.commit()


    '''
    *从用户组中移除用户
    * @param group_name, user_name
    * @return 
    '''
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
    def find_users_by_group_name(cls, group_name):
        group = UsergroupBusiness.find_group_by_name(group_name)

        for user in group.users:
            if user is not None:
                yield user
        pass

    ''' 
     * 根据用户名查找用户拥有的组信息
     * @param username
     * @return Set<group>
    '''
    @classmethod
    def find_group_by_user_name(cls, username):
        user = UserBusiness.find_user_by_name(username)

        for group in user.group:
            if group is not None:
                yield group

    @classmethod
    def add_users_into_group(cls, users, group_name):
        group = UsergroupBusiness.find_group_by_name(group_name)
        for user in users:
            if user is not None:
                group.users.append(user)

        db.session.commit()
        pass

    @classmethod
    def remove_users_from_group(cls, group_name, users):
        group = UsergroupBusiness.find_group_by_name(group_name)

        for user in users:
            if user in group.users:
                group.users.remove(user)
        db.session.commit()
        pass

# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness


class UserService(object):
    def __init__(self):
        pass

    # 用户查询
    @classmethod
    def user_query(cls, username=None, phone=None):
        user = UserBusiness.search_user_by_info(username, phone)

        organization = str(user['organization'])
        groups = user['group']
        for i in range(0, len(groups)):
            groups[i] = str(groups[i])

        return user

    # 用户更新
    @classmethod
    def user_update(cls, user_name, data):
        name = user_name
        user_obj = UserBusiness.update_user(name, data)
        return user_obj

    # 用户管理
    @classmethod
    def manage(cls, user, user_group, role):
        # 数据库添加用户
        UserBusiness.add_user(user)
        # 用户添加组
        if user_group is not None:
            user.group.append(user_group)
        # 用户添加角色
        # roles = find_all_roles()
        user.roles.append(role)
        pass

    # 根据角色名称查询用户信息
    @classmethod
    def find_users_by_role_name(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)
        for i in role.users:
            yield i
        pass

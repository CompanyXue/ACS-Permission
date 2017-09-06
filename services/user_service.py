# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness


class UserService(object):
    def __init__(self):
        pass

    # 用户更新
    @classmethod
    def user_update(cls, user_name, data):
        user = UserBusiness.find_user_by_name(user_name)
        user_obj = UserBusiness.update_user(user.id, data)
        print(user_obj.name + '--更新成功 ！！！')
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
  
    @classmethod
    def user_add(cls, data):
        user = UserBusiness.create_user(data)
        if type(user) == str:
            return user
        name = user.name
        oa = str(user.organization)
        # 同一个应用下，用户名唯一，也即name+org 唯一
        if UserBusiness.search_user_by_info(name=name, org=oa):
            # if UserBusiness.find_user_by_name(username):
            return "用户已存在,请重新输入！"
        else:
            UserBusiness.add_user(user)
            
        return user

    @classmethod
    def user_delete(cls, name, org):
        user = UserBusiness.find_user_by_org_name(org, name)
        if user:
            UserBusiness.delete_user_by_id(user.id)

    # 根据角色名称查询用户信息
    @classmethod
    def find_users_by_role_name(cls, role_name):
        role = RoleBusiness.find_by_role_name(role_name)
        for i in role.users:
            yield i
        pass

    # 根据用户 - 查询用户组信息
    
    @classmethod
    def find_groups_by_user_name(cls, org, user_name):
        user = UserBusiness.find_user_by_org_name(org, user_name)
        for i in user.group:
            yield i
        pass

# -*- coding: UTF-8 -*-

import database
from database.config_setting import date_time, app
from business.user_business import UserBusiness
from services.permission_service import PermissionService
from services.role_service import RoleService
from services.user_group_service import UserGroupService
from views import views

if __name__ == '__main__':

    users = UserBusiness.find_all_users()
    for i in users:
        print(i)

    print(date_time.strftime('%Y-%m-%d %H:%M:%S'))

    # PermissionService.add_permission_by_name('baidu')
    # PermissionService.delete_permission_by_name('除去用户')
    roles = PermissionService.find_roles_by_perm('添加用户')
    for i in roles:
        print(i)

    perms = PermissionService.find_perm_by_role('管理员Admin')
    for j in perms:
        print(j)

    PermissionService.add_permission_by_role_name('添加坐标', '管理员Admin')
    PermissionService.remove_permission_by_name('添加坐标', '管理员Admin')
    perms = PermissionService.find_perm_by_resource('新风设备1')
    for i in perms:
        print(i)

    res = RoleService.find_resource_by_role_name('管理员Admin')
    for i in res:
        print(i)

    groups = RoleService.find_group_by_role_name('管理员Admin')
    for i in groups:
        print(i)

    # UserGroupService.add_user_into_group('Rose','弱鸡')
    # UserGroupService.remove_user_from_group('Rose','弱鸡')

    users = UserGroupService.find_users_by_group_name('弱鸡')
    for i in users:
        print(i)

    groups = UserGroupService.find_group_by_user_name('Rose')
    for group in groups:
        print(group)

    app.run(debug=True)


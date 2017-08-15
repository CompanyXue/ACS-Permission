# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from database.models import  User, Role, Usergroup, db
from services.user_service import UserService
from services.role_service import RoleService
from services.permission_service import PermissionService

if __name__ == '__main__':
    
    roleservice = RoleService()
    # 测试 @根据用户名 查询所属角色
    roel = roleservice.find_role_by_uerid(14)
    for role in roel:
        if role is not None:
            print role
            
    # 测试 @根据角色名 查询用户       
    users = roleservice.find_users_by_rolename('SAAA')
    for user in users:
        if user is not None:
           print user
           
           
    xxxx = PermissionService()
    print xxxx
    perms = xxxx.find_all_permission()
    for per in perms:
        print per
        
    perms2 = xxxx.find_perm_by_role('系统管理员')
    print "start\n"
    for i in perms2:
        print i
    xxxx.add_permission_by_name('添加用户组')
    pass

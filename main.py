# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import time
from database.models import  User, Role, Usergroup, db, Permission
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
    perm = db.session.query(Permission).filter(Permission.name=='关注用户').one()
    # roleservice.add_permission_by_name(perm,'SAAA')
    print 'SAAA 添加qunxian'
           
           
    xxxx = PermissionService()
    print xxxx
    perms = xxxx.find_all_permission()
    for per in perms:
        print per
        
    perms2 = xxxx.find_perm_by_role('系统管理员')
    print "系统管理员 权限：start"
    for i in perms2:
        print i
   
    perms = xxxx.find_roles_by_perm('关注用户')
    for i in perms:
        print i
        
    time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    print time
    # 添加、删除 权限已测试成功
    # perm = Permission(name=u'添加用户组', o_type='3',create_time=time,content='Group Mamager TODO')
    # db.session.add(perm)
    # xxxx.add_permission_by_name(u'系统配置管理')
    # xxxx.delete_permission_by_name(u'系统设置管理')
    
    # roleservice.add_permission_by_name(u'系统配置管理','SAAA')
    perm = db.session.query(Permission).filter(Permission.name==u'系统配置管理').one()
    # roleservice.remove_permission_by_name(perm,u'系统管理员')
    print '添加角色权限，并移除之'
    
    #把 role表里id大于15的 role_code 全部更新成 Common Users
    db.session.query(Role).filter(Role.id > 15).update({'role_code' :'Common Users'})
    
    db.session.commit()
    pass

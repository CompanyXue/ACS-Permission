# -*- coding:utf-8 -*-
import hashlib
import time

from database.models import  User, Role, Usergroup, db
from services import user_service
from services.user_service import UserService
        
# 根据定义的表结构一键构建实体表
db.create_all()

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time 

# 加密用户密码
m = hashlib.md5()
m.update('987654321')

new_user = User(name='LeeB',sex='男', pwd=m.hexdigest(), phone='124234321323',\
                organization=u'如家酒店2', email='13142002124@qq.com',card_number=\
                '12145735622', is_activated='True', is_admin='True',
                create_time=time, create_by='SuperUser', status='close')

# 添加新用户到session:
db.session.add(new_user)
# 进行数据库交互, 但是事务并没有提交. 
db.session.flush()

# 添加新角色到 session:
new_role = Role(name='S3admin',role_type='1',create_time=time,is_activated='true')
db.session.add(new_role)
db.session.flush()

nenber = db.session.query(User).filter(User.name=='Brand').one()

nenber.add_role(new_role)
roles = nenber.get_roles()
print "用户-多角色显示："
for role in roles:
    if role is not None:
        print role
# x = User.query.with_parent(r_user_role) 
# print x

group = Usergroup(name=u'MEETING',create_time=time,is_activated=True)
db.session.add(group)
print group
nenber.group.append(group)

xxx = UserService()
print xxx
#查询所有用户列表
users = xxx.find_all_users()
for user in users:
    print user

# 通过用户id 来进行删除 (√)
user_service.delete_user_by_id(18)

#密码的更新，总提示参数不对。
# xxx.update_pwd(name='Brand',pwd=m.update('123'))

#输出根据id 去查询用户信息
print 'start\n'
user5 = xxx.find_user_by_id(5)
print 'user - id ==5:'
print user5

users = xxx.search_user_by_info('Brank','1762388223')
for user in users:
    print user
# 提交即保存到数据库:
db.session.commit()

# 测试用法 
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# role = db.session.query(Role).filter(Role.id=='5').one()
# 打印类型和对象的name属性:
# print 'type:', type(role)
# print 'role——name:', role.name
# print role


# users = db.session.query(User).all()
# user = db.session.query(User).filter(User.id=='2').one()
# print user

# 关闭session:
# db.session.close()

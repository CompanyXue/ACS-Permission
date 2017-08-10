# -*- coding:utf-8 -*-
import hashlib
import time

from database.models import  User, Role, db
from service.user_service import UserService


# 根据定义的表结构一键构建实体表
db.create_all()

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time 

# 加密用户密码
m = hashlib.md5()
m.update('1223243456')

new_user = User(name='Brank',sex='男',pwd=m.hexdigest(),phone='1762884223',organization=str('如家酒店').encode('utf-8'), email='13142344@qq.com',card_number='1039732',is_activated='True',is_admin='True',create_time=time,create_by='SuperUser',status='close')

new_role = Role(name='SSS',role_type='1',create_time=time,is_activated='true')
# 添加到session:
# db.session.add(new_role)

us = UserService.new()

# 添加到session:
# db.session.add(new_user)

# x = User.query.with_parent(r_user_role) 
# print x
# 提交即保存到数据库:
# db.session.commit()

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

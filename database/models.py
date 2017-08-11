# -*- coding: UTF-8 -*-

import hashlib
import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Date


# from service.user_service import UserService
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tomcat@127.0.0.1:3306/acs'
db = SQLAlchemy(app)

user2role = db.Table('r_user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('t_user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('t_role.id'))
)

user2group = db.Table('r_user_group',
    db.Column('user_id', db.Integer, db.ForeignKey('t_user.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('t_user_group.id'))
)

role2group = db.Table('r_group_role',
    db.Column('group_id', db.Integer, db.ForeignKey('t_user_group.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('t_role.id'))
)

role2perm = db.Table('r_role_permission',
    db.Column('perm_id', db.Integer, db.ForeignKey('t_permission.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('t_role.id'))
)

# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 't_user'

    id = Column(db.Integer, primary_key=True,autoincrement=True)
    name = Column(db.String(20), nullable=False,unique=True)
    phone = Column(db.String(20),nullable=False,unique=True)
    sex = Column(db.String(10),nullable=False)
    birthday = Column(db.Date(),nullable=True)
    pwd = Column(db.String(32),nullable=False)
    organization = Column(db.String(30),nullable=False)
    email = Column(db.String(20),nullable=False)
    card_number = Column(db.String(20),nullable=False,unique=True)
    create_by = Column(db.String(20),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    modified_date = Column(db.Date(),default=create_time)
    modified_by = Column(db.String(20),default=create_by)
    is_activated = Column(db.String(5),nullable=False)
    is_admin = Column(db.String(10),nullable=True)
    status = Column(db.String(10),nullable=False)
    
    #数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, email, card_number, create_time,create_by,is_activated, is_admin,status, _id=None):
        self.id = _id
        self.name = name
        self.sex = sex
        self.pwd = pwd
        self.phone = phone
        self.organization = organization
        self.email = email
        self.card_number = card_number
        self.is_activated = is_activated
        self.is_admin = is_admin
        self.create_time = create_time
        self.create_by = create_by
        # self.modified_date = modified_date
        # self.modified_by = modified_by
        self.status = status

    def __repr__(self):
        return "<User '{}'>".format('姓名：'+self.name +'\t性别：'+ self.sex +'\t组织：'+self.organization+'\t邮箱：'+\
            self.email+'\t电话号码：'+ self.phone+'\t卡号：'+self.card_number + '\t创建时间：'+str(self.create_time))
    
    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role

# 定义UserGroup对象
class UserGroup(db.Model):
    # 表的名字:
    __tablename__ = 't_user_group'

    id = Column(db.Integer, primary_key=True,autoincrement=True)
    name = Column(db.String(20), nullable=False,unique=True)
    create_time = Column(db.Date(),nullable=False)
    is_activated = Column(db.String(5),nullable=False)
    users = db.relationship('User', secondary=user2group,                     
        backref=db.backref('group', lazy='dynamic'))
    roles = db.relationship('Role', secondary=role2group,                     
        backref=db.backref('group', lazy='dynamic'))
    
    #数据表属性 初始化
    def __init__(self, name, role_type, is_activated, create_time, _id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.create_time = create_time
        self.is_activated = is_activated # 0-关闭 1-活动

    def __repr__(self):
        return "<UserGroup'{}'>".format('用户组名'+self.name + self.role_type + "创建时间："+str(self.create_time))

# 定义Role对象
class Role(db.Model):
    # 表的名字:
    __tablename__ = 't_role'

    # 表的结构:
    #primary_key等于主键
    #unique唯一
    #nullable非空
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    name = Column(db.String(20), nullable=False,unique=True)
    role_type = Column(db.String(20),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    is_activated = Column(db.String(5),nullable=False)
    users = db.relationship('User', secondary=user2role,                     
        #lazy='subquery', backref=db.backref('roles', lazy=True))
        backref=db.backref('roles', lazy='dynamic'))

    #数据表属性 初始化
    
    def __init__(self, name, role_type, is_activated, create_time, _id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.role_type = role_type   #管理员与普通身份    readonly 1 , modify 3, owner 4 
        self.create_time = create_time
        self.is_activated = is_activated

    def __repr__(self):
        return "<Role '{}'>".format('角色名'+self.name + self.role_type + "创建时间："+str(self.create_time))

class Log(db.Model):
    __tablename__ = 't_log'

    # 表的结构:
    #primary_key等于主键
    #unique唯一
    #nullable非空
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    op_type = Column(db.String(20),nullable=False)
    op_time = Column(db.String(20),nullable=False)
    user_id = Column(db.Integer, db.ForeignKey('t_user.id'))
    # user = db.relationship('User',
    #     backref=db.backref('posts', lazy='dynamic'))
    create_time = Column(db.Date(),nullable=False)
    content = Column(db.String(200))

    def __init__(self, name, role_type, create_time, _id=None):
        pass

class Resource(db.Model):
    __tablename__ = 't_resource'

    # 表的结构:
    #primary_key等于主键
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    name = Column(db.Integer, nullable=False)
    resource_type = Column(db.String(10),nullable=False)  
    owner = Column(db.Integer, db.ForeignKey('t_user.id'))
    # user = db.relationship('User',
    #     backref=db.backref('posts', lazy='dynamic'))
    create_time = Column(db.Date(),nullable=False)
    location = Column(db.String(100),nullable=True)
    content = Column(db.String(200))
    
class Permission(db.Model):
    __tablename__ = 't_permission'
    
    id = Column(db.Integer, primary_key=True,autoincrement=True)
    name = Column(db.Integer, nullable=False)
    type = Column(db.String(10),nullable=False)  
    opter = Column(db.Integer, db.ForeignKey('t_role.id'))
    user = Column(db.Integer, db.ForeignKey('t_user.id'))
    # user = db.relationship('User',
    #     backref=db.backref('posts', lazy='dynamic'))
    create_time = Column(db.Date(),nullable=False)
    resource = Column(db.Integer, db.ForeignKey('t_resource.id'))
    content = Column(db.String(200))
    
# class UserRole(db.Model):
#     __tablename__ = 'r_user_role'
#     关系最好不用Model创建，而是直接用定义的形式加入外键链接即可
#     id = Column(db.Integer, primary_key=True,autoincrement=True)
#     user_id = Column(db.Integer, db.ForeignKey('t_user.id'))
#     role_id = Column(db.Integer, db.ForeignKey('t_role.id'))



# class PermissionList(models.Model):
#     name = models.CharField(max_length=64)
#     url = models.CharField(max_length=255)

#     def __unicode__(self):
#         return '%s(%s)' %(self.name,self.url)
                                              
# class RoleList(models.Model):
#     name = models.CharField(max_length=64)
#     permission = models.ManyToManyField(PermissionList,null=True,blank=True)

#     def __unicode__(self):
#         return self.name
# 根据定义的表结构一键构建实体表
db.create_all()

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time 

# 加密用户密码
m = hashlib.md5()
m.update('1223243456')

new_user = User(name='Rose',sex='女',pwd=m.hexdigest(),phone='1234123527',organization=str('如家酒店').encode('utf-8'), email='1334942354@qq.com',card_number='103978034',is_activated='True',is_admin='True',create_time=time,create_by='SuperUser',status='close')

new_role = Role(name='SDE',role_type='2',create_time=time,is_activated='true')
# 添加新角色到session:
# db.session.add(new_role)

# 添加新用户到session:
# db.session.add(new_user)
n = db.session.query(User).filter(User.name=='Branky').one()

#举例说明
ro1 = db.session.query(Role).filter(Role.name=='SSE').one()
ro2 = db.session.query(Role).filter(Role.name=='SSS').one()
# ro1.users.append(n)
# n.roles = [ro1,ro2]
# new_role.users = [n,new_user]

# new_user.add_role(ro1)
# x = User.query.with_parent(r_user_role) 
# print x
# 提交即保存到数据库:
# db.session.commit()

    
# 测试用法 
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
role = db.session.query(Role).filter(Role.id=='1').one()
# 打印类型和对象的name属性:
print 'type:', type(role)
print 'role—name:', role.name
print role


# users = db.session.query(User).all()
user = db.session.query(User).filter(User.id=='5').one()
print user

# 关闭session:
# db.session.close()


# uer = UserManager.create_user('123','hello','123456')
# print user
# Permission.objects.create(name=u'权限管理',content_type_id=2,codename=u'权限管理描述')
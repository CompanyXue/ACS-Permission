# -*- coding: UTF-8 -*-

import hashlib
import time
from sqlalchemy import Column, String, Integer, Date, Boolean,Text
from sqlalchemy.types import BigInteger

from database.config_setting import db

# 关系没有用 Model 创建，而是直接用定义的形式加入外键链接即可,
# 定义：所有的关系表---规范为 mapping结尾，而实体属性表则用 英文名称 表示

user2role = db.Table('user_role_mapping',
                     db.Column('user_id', db.BigInteger,
                               db.ForeignKey('user.id'), primary_key=True),
                     db.Column('role_id', db.BigInteger,
                               db.ForeignKey('role.id'), primary_key=True)
                     )

user2group = db.Table('user_group_mapping',
                      db.Column('user_id', db.BigInteger,
                                db.ForeignKey('user.id'), primary_key=True),
                      db.Column('group_id', db.BigInteger,
                                db.ForeignKey('user_group.id'),
                                primary_key=True)
                      )

role2group = db.Table('group_role_mapping',
                      db.Column('group_id', db.BigInteger,
                                db.ForeignKey('user_group.id'),
                                primary_key=True),
                      db.Column('role_id', db.BigInteger,
                                db.ForeignKey('role.id'), primary_key=True)
                      )

role2perm = db.Table('role_permission_mapping',
                     db.Column('perm_id', db.BigInteger,
                               db.ForeignKey('permission.id'),
                               primary_key=True),
                     db.Column('role_id', db.BigInteger,
                               db.ForeignKey('role.id'), primary_key=True)
                     )

perm2resource = db.Table('resource_permission_mapping',
                         db.Column('perm_id', db.BigInteger,
                                   db.ForeignKey('permission.id'),
                                   primary_key=True),
                         db.Column('resource_id', db.BigInteger,
                                   db.ForeignKey('resource.id'),
                                   primary_key=True)
                         )


# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'user'
    
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), nullable=False, unique=True)
    phone = Column(db.String(20), unique=True)
    sex = Column(db.String(2))
    birthday = Column(db.Date())
    pwd = Column(db.String(256))
    organization = Column(db.String(100))
    email = Column(db.String(50), )
    card_number = Column(db.String(20), default='0001')
    create_by = Column(db.String(32))
    create_time = Column(db.Date())
    modified_date = Column(db.Date(), default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    status = Column(db.String(10), nullable=True, default='开启')
    is_deleted = Column(db.Boolean, default=False)


# 定义Role对象
class Role(db.Model):
    # 表的名字:
    __tablename__ = 'role'
    
    # 表的结构:
    # primary_key等于主键
    # unique唯一
    # nullable非空
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), nullable=False, unique=True)
    role_code = Column(db.String(30))
    role_type = Column(db.String(10))
    create_by = Column(db.String(32))
    create_time = Column(db.Date())
    modified_date = Column(db.Date(), default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    is_deleted = Column(db.Boolean, default=False)
    users = db.relationship('User', secondary=user2role,
                            backref=db.backref('roles', lazy='dynamic'))
    
    # 数据表属性 初始化
    def __init__(self, name, role_type, create_time, create_by, _id=None):
        self.id = _id
        self.name = name
        self.role_type = role_type  # 管理员与普通身份    readonly 1 , modify 3, owner 4
        self.create_by = create_by
        self.create_time = create_time


# 定义UserGroup对象
class Usergroup(db.Model):
    # 表的名字:
    __tablename__ = 'user_group'
    
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), nullable=False, unique=True)
    parent_name = Column(db.String(100))
    create_by = Column(db.String(32))
    create_time = Column(db.Date())
    modified_date = Column(db.Date(), default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    is_deleted = Column(db.Boolean, default=False)
    users = db.relationship('User', secondary=user2group,
                            backref=db.backref('group', lazy='dynamic',
                                               cascade='all, delete'))
    roles = db.relationship('Role', secondary=role2group,
                            backref=db.backref('group', lazy='dynamic',
                                               cascade='all, delete'))
    
    # 数据表属性 初始化
    def __init__(self, name, create_time, create_by, _id=None):
        self.id = _id
        self.name = name
        self.create_time = create_time
        self.create_by = create_by
        # self.is_activated = is_activated  # 0-关闭 1-活动
    
    def __repr__(self):
        return "<UserGroup'{}'>".format('用户组名' + self.name + "\t创建时间：" +
                                        str(self.create_time))
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)
    
    def add_users(self, users):
        for user in users:
            self.add_user(user)
    
    def get_users(self):
        for user in self.users:
            yield user
    
    def get_roles(self):
        for role in self.roles:
            yield role


class Resource(db.Model):
    __tablename__ = 'resource'
    
    # 表的结构:
    # primary_key等于主键
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), nullable=False, unique=True)
    res_type = Column(db.String(10))
    # owner = Column(db.Integer, db.ForeignKey('user.id'))
    create_time = Column(db.Date())
    create_by = Column(db.String(32))
    modified_date = Column(db.Date(), default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    location = Column(db.String(100), nullable=True)
    content = Column(db.Text)
    is_deleted = Column(db.Boolean, default=False)
    perms = db.relationship('Permission', secondary=perm2resource,
                            backref=db.backref('resources', lazy='dynamic',
                                               cascade='all, delete'))
    
    def __init__(self, name, res_type, create_time, create_by, is_deleted,
                 _id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.res_type = res_type  # 文件 1 , 门禁 2, 设备 3
        self.create_time = create_time
        self.create_by = create_by
        self.is_deleted = is_deleted
    
    def __repr__(self):
        return "<Role '{}'>".format(
            '资源名称' + self.name + '\t资源类型' + self.res_type + "创建时间："
            + str(self.create_time))


class Permission(db.Model):
    __tablename__ = 'permission'
    
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), nullable=False)
    o_type = Column(db.String(10))
    create_time = Column(db.Date())
    create_by = Column(db.String(32))
    modified_date = Column(db.Date(), default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    # resource = Column(db.Integer, db.ForeignKey('resource.id'))
    content = Column(db.Text)
    is_deleted = Column(db.Boolean, default=False)
    roles = db.relationship('Role', secondary=role2perm,
                            backref=db.backref('perms', lazy='dynamic',
                                               cascade='all, delete'))
    
    def __init__(self, name, o_type, create_time, create_by, content,
                 is_deleted, _id=None):
        self.id = _id
        self.name = name
        # self.pri_code = pri_code
        self.o_type = o_type
        self.create_by = create_by
        self.create_time = create_time
        self.content = content
        self.is_deleted = is_deleted
    
    def __repr__(self):
        return "<Permission '{}'>".format(
            '权限名称 :' + self.name + "\t类型：" + self.o_type + '\t权限内容：' +
            self.content + "\t创建时间：" + str(self.create_time))


# class PermissionList(models.Model):
#     name = models.CharField(max_length=64)
#     url = models.CharField(max_length=255)

#     def __unicode__(self):
#         return '%s(%s)' %(self.name,self.url)

# class RoleList(models.Model):
#     name = models.CharField(max_length=64)
#     permission = models.ManyToManyField(PermissionList,null=True,blank=True)

# 根据定义的表结构一键构建实体关系表
db.create_all()

time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(time)


# new_role = Role(name='SBE',role_code='ADministartor',role_type='2',create_time
# =time,is_activated='true')
# 添加新角色到session:
# db.session.add(new_role)

# 添加新用户到session:
# db.session.add(new_user)
# n = db.session.query(User).filter(User.name=='Branky').one()

# 举例说明
# ro1 = db.session.query(Role).filter(Role.name=='SSE').one()
# ro2 = db.session.query(Role).filter(Role.name=='SSS').one()
# ro1.users.append(n)
# n.roles = [ro1,ro2]
# new_role.users = [n,new_user]

# new_user.add_role(ro1)
# x = User.query.with_parent(r_user_role) 
# print x
# 提交即保存到数据库:
# db.session.commit()

# 关闭session:
# db.session.close()

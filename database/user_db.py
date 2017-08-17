# -*- coding: UTF-8 -*-

import time
from passlib.hash import sha256_crypt
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.types import BigInteger
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
# Base = declarative_base()

import config_setting
db = config_setting.db

# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'user'

    id = Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = Column(db.String(100), nullable=False,unique=True)
    phone = Column(db.String(20),nullable=False,unique=True)
    sex = Column(db.String(2),nullable=False)
    birthday = Column(db.Date(),nullable=True)
    pwd = Column(db.String(64),nullable=False)
    organization = Column(db.String(100),nullable=False)
    email = Column(db.String(50),nullable=False)
    card_number = Column(db.String(20),nullable=False,unique=True)
    create_by = Column(db.String(32),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    modified_date = Column(db.Date(),default=create_time)
    modified_by = Column(db.String(32),default=create_by)
    is_activated = Column(db.String(5),nullable=False)
    is_admin = Column(db.String(10),nullable=True)
    status = Column(db.String(10),nullable=True,default='开启')
    is_deleted = Column(db.Boolean,nullable=False,default=False)
    
    #数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, email, card_number,\
                 create_time,create_by,is_activated, is_admin,is_deleted, _id=None):
        self.id = _id
        self.name = name
        self.sex = sex
        self.pwd = sha256_crypt.encrypt(pwd)
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
        self.is_deleted = is_deleted

    def __repr__(self):
        if self.is_activated is not None:
            return "<User '{}'>".format('姓名：'+self.name +'\t性别：'+ self.sex +\
                                    '\t组织：'+self.organization+'\t邮箱：'+\
                                    self.email+'\t电话号码：'+self.phone+'\t卡号：'\
                                    + self.card_number + '\t创建时间：'\
                                    + str(self.create_time) + self.pwd)
    def verify(self, password):
        return sha256_crypt.verify(password, self.pwd)
    
    def add_role(self, role):
        self.roles.append(role)

    def add_roles(self, roles):
        for role in roles:
            self.add_role(role)

    def get_roles(self):
        for role in self.roles:
            yield role
            
    def add_user_group(self,group):
        self.group.append(group)
        
    def get_user_group(self):
        for group in self.group:
            yield group
    
    def reset_password(self, pwd):
        self.pwd = pwd
        pass
    
    # 传入参数更新用户可更改内容
    def update(data):
        self.name = data.name
        self.phone = data.phone
        self.email = data.email
        self.card_number = card_number
    #判断权限 是否有：role存在并且角色的权限要包含传入的权限  
    def can(self,permissions):
        return self.role is not None and \
            (self.roles.perms & permissions) == permissions
        
# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:tomcat@127.0.0.1:3306/acs')

# Base.metadata.create_all(engine) #创建所有表结构

# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

#创建与数据库的会话session class    
#注意,这里返回给session的是个class,不是实例 
#session = SessionCls()

# 创建session对象:
# session = DBSession()

# 根据定义的表结构一键构建实体表
# db.create_all()

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# my_user = User()
# my_user.add_roles('admin', 'superadmin')
# db.session.add(my_user)
# db.session.commit()
new_user = User(name='timy',sex='女',pwd='1234',phone='1762434223',organization=\
                u'如家酒店',email='13142341@qq.com',card_number='1032432',\
                is_activated='True',is_admin='True',create_time=time,\
                create_by='SuperUser',is_deleted=False)

# 添加到session:
db.session.add(new_user)

# 提交即保存到数据库:
# db.session.commit()

# 关闭session:
# db.session.close()

  
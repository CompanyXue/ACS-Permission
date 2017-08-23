# -*- coding: UTF-8 -*-

from config_setting import db
import user_db
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.types import BigInteger

user2role = db.Table('user_role_mapping',
    db.Column('user_id', db.BigInteger, db.ForeignKey('user.id'),primary_key=True),
    db.Column('role_id', db.BigInteger, db.ForeignKey('role.id'),primary_key=True)
)

# 定义Role对象
class Role(db.Model):
    # 表的名字:
    __tablename__ = 'role'

    # 表的结构:
    # primary_key等于主键
    # unique唯一
    # nullable非空
    id = Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = Column(db.String(100), nullable=False,unique=True)
    role_type = Column(db.String(10),nullable=False)
    create_by = Column(db.String(32),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    modified_date = Column(db.Date(),default=create_time)
    modified_by = Column(db.String(32),default=create_by)
    is_deleted = Column(db.Boolean,nullable=False,default=False)
    users = db.relationship('User', secondary=user2role, \
                            backref=db.backref('roles', lazy='dynamic'))

    #数据表属性 初始化
    def __init__(self, name, role_type, create_time, create_by, _id=None):
        self.id = _id
        self.name = name
        self.role_type = role_type   #管理员与普通身份    readonly 1 , modify 3, owner 4
        self.create_by = create_by
        self.create_time = create_time

    def __repr__(self):
        return "<Role '{}'>".format('角色名：'+self.name +'\t角色类型：'+ self. \
                                         role_type + "\t创建时间："+str(self.create_time))
    
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)
        pass
    
    def add_users(self, users):
        for user in users:
            self.add_user(user)

    def get_users(self):
        for user in self.users:
            yield user
            
    def add_role_group(self,group):
        self.group.append(group)
        
    def get_role_group(self):
        for group in self.group:
            yield group

    def add_role_permission(self,perm):
        self.perms.append(perm)
        
    def get_role_permission(self):
        for perm in self.perms:
           yield perm

# -*- coding: UTF-8 -*-

from sqlalchemy import Table, Column, ForeignKey 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import BigInteger, String, Date, Boolean, DateTime
from database import user_db
from database.config_setting import db, date_time

user2role = db.Table('user_role_mapping',
                     db.Column('user_id', db.BigInteger,
                               db.ForeignKey('user.id'), primary_key=True),
                     db.Column('role_id', db.BigInteger,
                               db.ForeignKey('role.id'), primary_key=True)
                     )


# 定义Role对象
class Role(db.Model):
    # 表的名字:
    __tablename__ = 'role'

    # 表的结构:
    # primary_key等于主键
    # unique唯一
    # nullable非空
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), unique=True)
    role_type = Column(db.String(10))
    create_by = Column(db.String(32))
    create_time = Column(db.DateTime, default=date_time)
    modified_date = Column(db.DateTime, default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    is_deleted = Column(db.Boolean, default=False)
    users = relationship('User', secondary=user2role,
                         backref=backref('roles', lazy='dynamic',
                                         cascade='all, delete'))

    # 数据表属性 初始化
    def __init__(self, name, role_type, create_by, _id=None):
        self.id = _id
        self.name = name
        self.role_type = role_type
        self.create_by = create_by

    def __repr__(self):
        return "<Role '{}'>".format(
            '角色名：' + self.name + '\t角色类型：' + self.role_type + "\t创建时间："
            + str(self.create_time))

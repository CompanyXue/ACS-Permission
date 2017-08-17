# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.types import BigInteger

import config_setting
db = config_setting.db


class Resource(db.Model):
    __tablename__ = 'resource'

    # 表的结构:
    id = Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = Column(db.String(100), nullable=False,unique=True)
    res_type = Column(db.String(10),nullable=False)
    # owner = Column(db.Integer, db.ForeignKey('user.id'))
    location = Column(db.String(100),nullable=True)
    create_by = Column(db.String(32),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    modified_date = Column(db.Date(),default=create_time)
    modified_by = Column(db.String(32),default=create_by)
    is_deleted = Column(db.Boolean,nullable=False,default=False)
    content = Column(db.String(200))

    def __init__(self, name, resource_type, is_activated, create_time,create_by\
                 ,is_deleted,_id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.resource_type = role_type   # 文件 1 , 门禁 2, 设备 3 
        self.create_time = create_time
        self.create_by = create_by
        self.is_activated = is_activated
        self.is_deleted = is_deleted

    def __repr__(self):
        return "<Role '{}'>".format('资源名称'+self.name + '\t资源类型'+ self.resource_type\
                                    + "创建时间："+str(self.create_time))
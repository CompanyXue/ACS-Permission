# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Date, Boolean, DateTime
from sqlalchemy.types import BigInteger
from database.config_setting import db, date_time

perm2resource = db.Table('resource_permission_mapping',
                         db.Column('perm_id', db.BigInteger,
                                   db.ForeignKey('permission.id'),
                                   primary_key=True),
                         db.Column('resource_id', db.BigInteger,
                                   db.ForeignKey('resource.id'),
                                   primary_key=True)
                         )


class Resource(db.Model):
    __tablename__ = 'resource'

    # 表的结构:
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), unique=True)
    res_type = Column(db.String(10))
    location = Column(db.String(100))
    content = Column(db.Text, default='')
    # owner = Column(db.Integer, db.ForeignKey('user.id'))
    create_time = Column(db.DateTime, default=date_time)
    create_by = Column(db.String(32))
    modified_date = Column(db.DateTime, default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    is_deleted = Column(db.Boolean, default=False)
    perms = db.relationship('Permission', secondary=perm2resource,
                            backref=db.backref('resources', lazy='dynamic',
                                               cascade='all, delete'))

    def __init__(self, name, res_type, location, create_by, _id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.res_type = res_type  # 文件 1 , 门禁 2, 设备 3
        self.location = location
        self.create_by = create_by

    def __repr__(self):
        return "<Role '{}'>".format('资源名称: ' + self.name + '\t资源类型: ' +
                          self.res_type + "\t创建时间：" + str(self.create_time))

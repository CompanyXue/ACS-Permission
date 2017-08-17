# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.types import BigInteger

import user_db, role_db
import config_setting
db = config_setting.db


role2perm = db.Table('role_permission_mapping',
    db.Column('perm_id', db.BigInteger, db.ForeignKey('permission.id'),primary_key=True),
    db.Column('role_id', db.BigInteger, db.ForeignKey('role.id'),primary_key=True)
)

class Permission(db.Model):
    __tablename__ = 'permission'
    
    id = Column(db.BigInteger, primary_key=True,autoincrement=True)
    name = Column(db.String(100), nullable=False)
    o_type = Column(db.String(10),nullable=False)  
    create_time = Column(db.Date(),nullable=False)
    create_by = Column(db.String(32),nullable=False)
    create_time = Column(db.Date(),nullable=False)
    modified_date = Column(db.Date(),default=create_time)
    modified_by = Column(db.String(32),default=create_by)
    # resource = Column(db.Integer, db.ForeignKey('resource.id'))
    content = Column(db.Text)
    roles = db.relationship('Role', secondary=role2perm,
                            backref=db.backref('perms', lazy='dynamic'))
    
	#数据表属性 初始化
    def __init__(self, name, o_type, create_time,create_by, content, _id=None):
        self.id = _id
        self.name = name
        # self.pri_code = pri_code
        self.o_type = o_type
        self.create_by = create_by
        self.create_time = create_time
        self.content = content

    def __repr__(self):
        return "<Permission '{}'>".format('权限名称 :'+self.name + "\t类型："+self.o_type\
                                          + '\t权限内容：'+ self.content+"\t创建时间："\
                                          + str(self.create_time))

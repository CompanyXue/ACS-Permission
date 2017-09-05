# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.types import BigInteger
from database.config_setting import db, date_time

role2perm = db.Table('role_permission_mapping',
                     db.Column('perm_id', db.BigInteger,
                               db.ForeignKey('permission.id'),
                               primary_key=True),
                     db.Column('role_id', db.BigInteger,
                               db.ForeignKey('role.id'),
                               primary_key=True)
                     )


class Permission(db.Model):
    __tablename__ = 'permission'
    
    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), unique=True)
    o_type = Column(db.String(10))
    create_by = Column(db.String(32))
    create_time = Column(db.DateTime, default=date_time)
    modified_date = Column(db.DateTime, default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    # resource = Column(db.BigInteger, db.ForeignKey('resource.id'))
    content = Column(db.Text)
    is_deleted = Column(db.Boolean, default=False)
    roles = db.relationship('Role', secondary=role2perm,
                            backref=db.backref('perms', lazy='dynamic',
                                               cascade='all, delete'))
    
    def __init__(self, name, o_type, create_by, content, _id=None):
        self.id = _id
        self.name = name
        self.o_type = o_type
        self.create_by = create_by
        self.content = content

    def __repr__(self):
        return "<Permission '{}'>".format(
            '权限名称 :' + self.name + "\t类型：" + self.o_type + '\t权限内容：' +
            self.content + "\t创建时间：" + str(self.create_time))
        pass

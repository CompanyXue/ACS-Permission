# -*- coding: UTF-8 -*-

from database.config_setting import db, date_time
from sqlalchemy import Column

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


# 定义UserGroup对象
class Usergroup(db.Model):

    __tablename__ = 'user_group'

    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), unique=True)
    parent_name = Column(db.String(100), default='Basic')
    create_by = Column(db.String(32))
    create_time = Column(db.DateTime, default=date_time)
    modified_date = Column(db.DateTime, default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    is_deleted = Column(db.Boolean, default=False)
    users = db.relationship('User', secondary=user2group,
                            backref=db.backref('group', lazy='dynamic'))
    roles = db.relationship('Role', secondary=role2group,
                            backref=db.backref('group', lazy='dynamic'))

    # 数据表属性 初始化
    def __init__(self, name, create_by, _id=None):
        self.id = _id
        self.name = name
        self.create_by = create_by
        # self.is_activated = is_activated  # 0-关闭 1-活动

    def __repr__(self):
        return "<UserGroup'{}'>".format('用户组名: ' + self.name + "\t创建时间：" \
                                        + str(self.create_time))

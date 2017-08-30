# -*- coding: UTF-8 -*-

from database.config_setting import db
from database.user_group_db import Usergroup


class UsergroupBusiness(object):
    def __init__(self):
        pass

    # 查询全部用户组信息
    @classmethod
    def find_all_groups(cls):
        groups = db.session.query(Usergroup).all()
        for i in groups:
            yield i
        pass

    # 根据名称查询用户组信息
    @classmethod
    def find_group_by_name(cls, group_name):
        group = db.session.query(Usergroup).filter_by(name=group_name).first()
        if group is not None:
            return group

    '''
    * 添加用户组
    * @param group_name
    * @return 
    '''
    @classmethod
    def add_user_group(cls, group_name):
        group = Usergroup(name=group_name, create_by='SuperUser')
        if group_name:
            print('添加用户组：', group)
            db.session.add(group)
            db.session.commit()

    '''
    * 删除用户组
    * @param group_name
    * @return 
    '''
    @classmethod
    def delete_user_group(cls, group_name):
        group = cls.find_group_by_name(group_name)
        if group is not None:
            print('删除用户组：', group)
            db.session.delete(group)
            db.session.commit()
        pass

# -*- coding: UTF-8 -*-

from app import db
from flask.ext.permissions.models import UserMixin

class User(UserMixin):
    #数据表属性 初始化
    def __init__(self, phone, sex, pwd, organization, groups, role_group_id, name, mail, card_number, is_activated, is_admin, _id=None):
        self._id = _id
        self.sex = sex
        self.pwd = pwd
        self.name = name
        self.phone = phone
        self.organization = organization
        self.groups = groups
        self.mail = mail
        self.card_number = card_number
        self.is_activated = is_activated
        self.is_admin = is_admin
        UserMixin.__init__(self, roles)
       

    def set():
       pass

    def get():
        pass


my_role = Role('admin')
my_role.add_abilities('create_users', 'delete_users', 'bring_about_world_peace')
db.session.add(my_role)
db.session.commit()

my_user = User()
my_user.add_roles('admin', 'superadmin')
db.session.add(my_user)
db.session.commit()
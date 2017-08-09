# -*- coding: UTF-8 -*-

class User:
    # 表的名字:
    __tablename__ = 't_user'

    #数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, groups, mail, card_number, is_activated, is_admin, create_date,create_by,status, _id=None):
        self.id = _id
        self.name = name
        self.sex = sex
        self.pwd = pwd
        self.phone = phone
        self.organization = organization
        self.groups = groups
        self.mail = mail
        self.card_number = card_number
        self.is_activated = is_activated
        self.is_admin = is_admin
        self.create_date = create_date
        self.create_by = create_by
        self.status = status

    def set():
       pass

    def get():
        pass


# my_role = Role('admin')
# my_role.add_abilities('create_users', 'delete_users', 'bring_about_world_peace')
# db.session.add(my_role)
# db.session.commit()

# my_user = User()
# my_user.add_roles('admin', 'superadmin')
# db.session.add(my_user)
# db.session.commit()

  
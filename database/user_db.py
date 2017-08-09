# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String, Integer, Date

class User:
    # 表的名字:
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(20),nullable=False)
    sex = Column(String(10),nullable=False)
    birthday = Column(Date(),nullable=True)
    pwd = Column(String(20),nullable=False)
    organization = Column(String(30),nullable=False)
    email = Column(String(20),nullable=False)
    card_number = Column(String(20),nullable=False)
    create_by = Column(String(20),nullable=False)
    create_time = Column(Date(),nullable=False)
    is_activated = Column(String(10),nullable=False)
    status = Column(String(10),nullable=False)


    #数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, email, card_number, is_activated, is_admin, create_date,create_by,status, _id=None):
        self.id = _id
        self.name = name
        self.sex = sex
        self.pwd = pwd
        self.phone = phone
        self.organization = organization
        self.email = email
        self.card_number = card_number
        self.is_activated = is_activated
        self.is_admin = is_admin
        self.create_date = create_date
        self.create_by = create_by
        # self.modified_date = modified_date
        # self.modified_by = modified_by
        self.status = status


# my_role = Role('admin')
# my_role.add_abilities('create_users', 'delete_users', 'bring_about_world_peace')
# db.session.add(my_role)
# db.session.commit()

# my_user = User()
# my_user.add_roles('admin', 'superadmin')
# db.session.add(my_user)
# db.session.commit()

  
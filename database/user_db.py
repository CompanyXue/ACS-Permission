# -*- coding: UTF-8 -*-

import time,sys
from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
reload(sys)
sys.setdefaultencoding('utf-8')

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(20),nullable=False)
    sex = Column(String(10),nullable=False)
    birthday = Column(Date(),nullable=True)
    pwd = Column(String(32),nullable=False)
    organization = Column(String(30),nullable=False)
    email = Column(String(20),nullable=False)
    card_number = Column(String(20),nullable=False)
    create_by = Column(String(20),nullable=False)
    create_time = Column(Date(),nullable=False)
    modified_date = Column(Date(),default=create_time)
    modified_by = Column(String(20),default=create_by)
    is_activated = Column(String(10),nullable=False)
    is_admin = Column(String(10),nullable=True)
    status = Column(String(10),nullable=False)

    #数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, email, card_number, create_time,create_by,is_activated, is_admin,status, _id=None):
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
        self.create_time = create_time
        self.create_by = create_by
        # self.modified_date = modified_date
        # self.modified_by = modified_by
        self.status = status

    def __repr__(self):
        return "<User '{}'>".format('姓名：'+self.name +'\t性别：'+ self.sex +'\t组织：'+self.organization+'\t邮箱：'+\
            self.email   +'\t电话号码：'+ self.phone + '\t创建时间：'+str(self.create_time))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:tomcat@127.0.0.1:3306/acs')

Base.metadata.create_all(engine) #创建所有表结构

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time
# my_user = User()
# my_user.add_roles('admin', 'superadmin')
# db.session.add(my_user)
# db.session.commit()
new_user = User(name='Bob',sex='男',pwd=hash('123456'),phone='13243434434',organization=str('如家酒店').encode('utf-8'), email='13142341@qq.com',card_number='102312',is_activated='True',is_admin='True',create_time=time,create_by='SuperUser',status='开启')

# 添加到session:
session.add(new_user)

# 提交即保存到数据库:
session.commit()

# users = User.query.all()
user = session.query(User).filter(User.id=='2').one()
print user

# 关闭session:
session.close()

  
# -*- coding: UTF-8 -

from database.config_setting import db, date_time
from passlib.hash import sha256_crypt
from sqlalchemy import Column, String, Date, Boolean, DateTime
from sqlalchemy.types import BigInteger


# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
# Base = declarative_base()


# 定义User对象:
class User(db.Model):
    # 表的名字:
    __tablename__ = 'user'

    id = Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = Column(db.String(100), unique=True)
    phone = Column(db.String(20), unique=True)
    sex = Column(db.String(2))
    birthday = Column(db.Date())
    pwd = Column(db.String(256))
    organization = Column(db.String(100))
    email = Column(db.String(50))
    card_number = Column(db.String(20), default='0001')
    create_by = Column(db.String(32))
    create_time = Column(db.DateTime, default=date_time)
    modified_date = Column(db.DateTime, default=create_time)
    modified_by = Column(db.String(32), default=create_by)
    status = Column(db.String(10), default='开启')
    is_deleted = Column(db.Boolean, default=False)

    # 数据表属性 初始化
    def __init__(self, name, phone, sex, pwd, organization, email, create_by, _id=None):
        self.id = _id
        self.name = name
        self.phone = phone
        self.sex = sex
        self.pwd = sha256_crypt.encrypt(pwd)
        self.organization = organization
        self.email = email
        self.create_by = create_by

    def __repr__(self):
        return "<User '{}'>".format(
            '姓名：' + self.name + '\t性别：' + self.sex + '\t组织：' +
            self.organization + '\t邮箱：' + self.email + '\t电话号码：' +
            self.phone + '\t 卡号：' + self.card_number + '\t创建时间：' +
            str(self.create_time) + '\tBy:' + self.create_by)

    # 判断权限 是否有：role存在并且角色的权限要包含传入的权限
    def can(self, permissions):
        return self.role is not None and \
               (self.roles.perms & permissions) == permissions


# 初始化数据库连接:
# engine = create_engine('mysql+pymysql://root:tomcat@127.0.0.1:3306/acs')

# Base.metadata.create_all(engine) #创建所有表结构

# 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

# 创建与数据库的会话session class
# 注意,这里返回给session的是个class,不是实例
# session = SessionCls()

# 创建session对象:
# session = DBSession()

# 根据定义的表结构一键构建实体表
# db.create_all()

# my_user = User()
# my_user.add_roles('admin', 'superadmin')
# db.session.add(my_user)
# db.session.commit()
new_user = User(name='Romo', sex='女', pwd='userp', phone='1762434203',
                organization=u'如家酒店', email='13142391@qq.com', create_by='U')

# 添加到session:
# db.session.add(new_user)

# 提交即保存到数据库:
db.session.commit()

# 关闭session:
# db.session.close()

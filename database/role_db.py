# -*- coding: UTF-8 -*-


import time
from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Role对象
class Role(Base):
    # 表的名字:
    __tablename__ = 't_role'

    # 表的结构:
    #primary_key等于主键
    #unique唯一
    #nullable非空
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20), nullable=False)
    role_type = Column(String(20),nullable=False)
    create_time = Column(Date(),nullable=False)
    is_activated = Column(String(10),nullable=False)

    #数据表属性 初始化
    
    def __init__(self, name, role_type, is_activated, create_time, _id=None):
        self.id = _id
        # self.role_group_id = role_group_id  
        self.name = name
        self.role_type = role_type   #管理员与普通身份    readonly 1 , modify 3, owner 4 
        self.create_time = create_time
        self.is_activated = is_activated

	def __repr__(self):
        return "<Role '{}'>".format(self.name + self.role_type +self.create_time)

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:tomcat@127.0.0.1:3306/acs')

Base.metadata.create_all(engine) #创建所有表结构

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
#bind绑定
#创建与数据库的会话session class    
#注意,这里返回给session的是个class,不是实例 
#session = SessionCls()

# 创建session对象:
session = DBSession()
# 创建新role对象:
time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time
new_role = Role(name='SYSTEM',role_type='3',create_time=time,is_activated='true')
# 添加到session:
session.add(new_role)

# 测试用法 
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(Role).filter(Role.id=='2').one()
# 打印类型和对象的name属性:
# print 'type:', type(user)
# print 'role——name:', user.name

# 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()

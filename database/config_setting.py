# -*-coding:utf-8 -*-  

import time
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 调用Flask App和 SQLAlchemy 组件，创建与数据库的连接
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tomcat@127.0.0.1:3306/acs'
db = SQLAlchemy(app)

# app.run(debug=True)

date_now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# 国际时间
date_time = datetime.utcnow()
# 本地时间
date_time = datetime.now()

# 根据定义的表结构一键构建实体表
def init_db():
    db.create_all()
  
# 删除数据库表  
def drop_db():
    db.drop_all()
    
#sqlalchemy.orm.exc.UnmappedInstanceError 异常
#sqlalchemy.orm.exc.UnmappedInstanceError: Class '__builtin__.instance' is not mapped
# 'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead 。。。改为True

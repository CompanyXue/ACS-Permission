# -*-coding:utf-8 -*-  

import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 调用Flask App和 SQLAlchemy 组件，创建与数据库的连接
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tomcat@127.0.0.1:3306/acs'
db = SQLAlchemy(app)

# app.run(debug=True)

time_now = time.strftime('%Y-%m-%d',time.localtime(time.time()))

#sqlalchemy.orm.exc.UnmappedInstanceError 异常
#sqlalchemy.orm.exc.UnmappedInstanceError: Class '__builtin__.instance' is not mapped
# 'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead 。。。改为True

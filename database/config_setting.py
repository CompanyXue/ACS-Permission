# -*-coding:utf-8 -*-  

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Date, Boolean

# 调用Flask App和 SQLAlchemy 组件，创建与数据库的连接
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tomcat@127.0.0.1:3306/ACS'
db = SQLAlchemy(app)

class Config(object):
	pass
	
class DevConfig(Config):
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
	# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@127.0.0.1:3306/acs"


#sqlalchemy.orm.exc.UnmappedInstanceError 异常
#sqlalchemy.orm.exc.UnmappedInstanceError: Class '__builtin__.instance' is not mapped
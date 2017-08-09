# -*-coding:utf-8 -*-  

class Config(object):
	pass
	
class ProdConfig(Config):
	pass
	
class DevConfig(Config):
	DEBUG = True
	#SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@127.0.0.1:3306/acs"


#sqlalchemy.orm.exc.UnmappedInstanceError 异常
#sqlalchemy.orm.exc.UnmappedInstanceError: Class '__builtin__.instance' is not mapped
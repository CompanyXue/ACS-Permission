# -*- coding: UTF-8 -*-

from config_setting import db

class BaseModel(db.Model):
    class Metadata(object):
        #code
        database = 'database'
    
    

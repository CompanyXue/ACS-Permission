# -*- coding: UTF-8 -*-
import sys

sys.path.append("..")
from database.config_setting import db, date_time
from database.resource_db import Resource


class ResourceBusiness(object):
    def __init__(self):
        pass

    '''
    * 查询全部（门禁）资源信息
    * @return List<Resource> 
    '''
    @classmethod
    def find_all_resource(cls):
        resources = db.session.query(Resource).all()
        for re in resources:
            yield re

    '''
     * 根据名称获取该用户可访问的资源
     * @param res_name
     * @return
    '''

    @classmethod
    def find_by_name(cls, res_name):
        resource = db.session.query(Resource).filter_by(name=res_name).first()
        if resource is not None:
            return resource

    @classmethod
    def add_resource(cls, res):
        db.session.add(res)
        db.session.commit()
        pass

    @classmethod
    def delete_resource(cls, res):
        db.session.delete(res)
        db.session.commit()
        pass

    @classmethod
    def update_resource(cls, res):
        resource = self.find_by_name(res.name)
        resource.modified_date = date_time
        resource.__dict__.update()
        db.session.commit()
        pass

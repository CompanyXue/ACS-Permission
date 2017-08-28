# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from database.config_setting import db, date_time
from database.permission_db import Permission
from database.resource_db import Resource

class ResourceBusiness(object):
	
    '''
    * 查询全部（门禁）资源信息
    * @return List<Resource> 
    '''
    @classmethod
    def find_all_resource():
        resources = Resource.query().all()
        for re in resources:
            yield re
    
	
    '''
     * 根据用户角色获取该用户可访问的资源（权限）
     * @param userId
     * @return
    '''
    @classmethod
    def find_resources_by_role(role):
        
       pass
    
    @classmethod
    def add_resource(self, res):
       db.session.add(res)
       db.session.commit()
       pass







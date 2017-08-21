# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from database.config_setting import db
from database.permission_db import Permission
from database.role_db import Role
from database.resource_db import Resource

class ResourceBusiness(object):
	'''
	 * 查询全部（门禁）资源信息
	 * @return List<Resource> 
	 '''
	def find_all_resource():
		resources = db.session.query('Resource').all()
		for re in resources:
			yield re
		pass

	'''
	 * 根据用户角色获取该用户可访问的资源（权限）
	 * @param userId
	 * @return
	 '''
	def find_resources_by_role(role):
		
		pass




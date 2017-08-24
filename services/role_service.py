# -*- coding: UTF-8 -*-

from business.user_business import UserBusiness
from business.role_business import RoleBusiness
from business.user_group_business import UsergroupBusiness

class RoleService(object):
	
	def __init__(self):
		'''
		Constructor
		'''
		
	# 根据用户角色名查找有哪些用户
	# @param role_name
	# @return users
	def find_users_by_rolename(self, role_name):
	
		pass
	
	''' 
	* 根据用户名查找用户拥有的角色信息
	* 根据角色id 刪除角色
	* @param role_id
	* @return role
	'''
	def add_role_by_name(self,role_id):
		
		pass
	
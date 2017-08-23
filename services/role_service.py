# -*- coding: UTF-8 -*-
from config_setting import db

class RoleService(object):
	
	def __init__(self):
		'''
		Constructor
		'''
		
	# 根据用户角色名查找有哪些用户
	# @param role_name
	# @return users
	def find_users_by_rolename(self, role_name):
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None:
			for user in role.users:
				if user is not None:
					yield user
				# print user
	
	
	''' 
	 * 根据用户名查找用户拥有的角色信息
	 * @param username
	 * @return roles
	 '''
	def find_role_by_user_name(self, user_name):
		user = db.session.query(User).filter(User.name==user_name).first()
		if user is not None:
			for role in user.roles:
				if role is not None:
					yield role
		pass
	
	'''
	* 根据角色id 刪除角色
	* @param role_id
	* @return role
	'''
	def add_role_by_name(self,role_id):
		role = db.session.query(Role).filter(Role.id==role_id).first()
		if role is not None:
			db.session.delete(role)
			yield role
		pass
	
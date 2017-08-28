# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from database.config_setting import db, date_time
from database.user_db import User
from database.role_db import Role
from database.permission_db import Permission

class RoleBusiness(object):
	
	def __init__(self):
		'''
		Constructor
		'''
	
	# 查询全部角色信息
	def find_all_roles(self):
		roles = db.session.query(Role).all()
		for i in roles:
			yield i
		pass
	
	# 根据用户角色名查找有哪些用户
	# @param role_name
	# @return 
	def find_users_by_rolename(self, role_name):
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None:
			for user in role.users:
				if user is not None:
					yield user
				# print user
	
	'''
	 * 根据用户的Id查找用户的角色信息
	 * @param userId
	 * @return
	 '''
	def find_role_by_uerid(self, user_id):
		user = db.session.query(User).filter(User.id==user_id).first()
		if user is not None:
			for role in user.roles:
				if role is not None:
					yield role
		pass
	
	''' 
	 * 根据用户名查找用户拥有的角色信息
	 * @param username
	 * @return Set<Role>
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
			db.session.commit()
			yield role
		pass
	
	'''
	* 根据名稱刪除角色
	* @param role_name
	* @return role
	'''
	def delete_role_by_name(self,role_name):
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None:
			db.session.delete(role)
			db.session.commit()
			yield role
		pass

	'''
	* 根据名稱添加用户的权限
	* @param role_name
	* @return role
	'''
	def add_permission_by_name(self, perm_name, role_name):
		perm = db.session.query(Permission).filter(Permission.name==perm_name).first()
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None and perm is not None:
			role.perms.append(perm)
			
		db.session.commit()
		pass
	
	'''
	* 根据名稱移除角色的权限
	* @param role_name
	* @return role
	'''
	def remove_permission_by_name(self, perm, role_name):
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None :
			if perm in role.perms:
				role.perms.remove(perm)
				role.modified_date = date_time
				db.session.commit()
		pass
	
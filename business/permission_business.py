# -*- coding: UTF-8 -*-
import time
import sys
sys.path.append("..")
# from database.models import Permission,Role,db
from database.config_setting import db
from database.permission_db import Permission
from database.role_db import Role

time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

class PermissionBusiness(object):
	
	def __init__(self):
		'''
		Constructor
		'''
	
	# 查询出所有的权限列表
	def find_all_permission(self):
		perms = db.session.query(Permission).all()
		for re in perms:
			if re is not None:
				yield re
		pass

	'''
	 * 根据用户角色获取该用户的权限
	 * @param role_name
	 * @return perm set
	'''
	def find_perm_by_role(self,role_name):
		role = db.session.query(Role).filter(Role.name==role_name).first()
		if role is not None:
			for perm in role.perms:
				if perm is not None:
					yield perm
		pass
	
	'''
	* 根据权限名称获取用户角色
	* @param perm_name
	* @return role set
	'''
	def find_roles_by_perm(self, perm_name):
		perm = db.session.query(Permission).filter(Permission.name==perm_name).first()
		if perm is not None:
			for role in perm.roles:
				if role is not None:
					yield role
		pass
	
	'''
	* 根据权限名字刪除用户的权限
	* @param perm_name
	* @return perm
	'''
	def add_permission_by_name(self,perm_name):
		print (u'类中的时间: ',time)
		perms = Permission(name=str(perm_name), o_type='2', create_time=time,\
						  content='TODO ')
		print '添加权限XXX'
		db.session.add(perms)
		print '添加成功'
	

	'''
	* 根据权限名字刪除用户的权限
	* @param perm_name
	* @return perm
	'''
	def delete_permission_by_name(self,perm_name):
		perm = db.session.query(Permission).filter(Permission.name==perm_name).first()
		if perm is not None:
			print perm
			db.session.delete(perm)
		pass

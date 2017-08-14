# -*- coding: UTF-8 -*-

class PermissionService(object):
	
	def __init__(self):
		'''
		Constructor
		'''
	
	# 查询出所有的权限列表
	def find_all_permission(self):
		perm = db.session.query(Permission).all()
		for re in perm:
			yield re
		pass

	'''
	 * 根据用户角色获取该用户的权限
	 * @param role_name
	 * @return perm set
	'''
	def find_perm_by_role(self,role_name):
		role = db.session.query(Role).filter(Role.name==role_name).one()
		for perm in role.permission:
			if perm is not None:
				yield perm
		pass
	
	'''
	* 根据用户角色获取该用户的权限
	* @param perm_name
	* @return role set
	'''
	def find_roles_by_perm(perm_name):
		perm = db.session.query(Permission).filter(Permission.name==perm_name).one()
		for role in perm.roles:
			if role is not None:
				yield role
		pass
	





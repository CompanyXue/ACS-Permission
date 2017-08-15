# -*- coding: UTF-8 -*-

class UserGroupService(object):
	
	def __init__(self):
		'''
		Constructor
		'''
		
	'''
	 * 根据用户组名查找有哪些用户
	 * @param role_name
	 * @return 
	'''
	def find_users_by_group_name(self, group_name):
		group = db.session.query(Group).filter(Group.name==group_name).one()
		for user in group.users:
			if user is not None :
				yield user
		pass
	
	'''
	 * 插入数据到user_role_mapping做关联关系
	 * @param userRoles
	 * @return
	'''
	def add_users_into_group(users,group):
		for user in users:
			if user is not None:
				group.users.append(users)
		pass
	
	''' 
	 * 根据用户名查找用户拥有的组信息
	 * @param username
	 * @return Set<Role>
	'''
	def find_group_by_user_name(self,username):
		user = db.session.query(User).filter(User.name==username).one()
		for group in user.group:
			if group is not None:
				yield group
		pass
	
	'''
	*从用户组中移除用户
	* @param group_name, users
	* @return 
	'''
	def remove_users_from_group(self, group_name, users):
		group = db.session.query(Group).filter(Group.name==group_name).one()
		if group is not None:
			for user in users:
				if user in group.users:
				    group.users.remove(user)
		else:
			if users in group.users:
				group.users.remove(users)
		pass
	
	'''
	* 删除用户组
	* @param group_name
	* @return 
	'''
	def delete_user_group(self, group_name):
		group = db.session.query(Group).filter(Group.name==group_name).one()
		if group is not None:
			print '删除用户组：', group
			db.session.delete(group)
		pass
	
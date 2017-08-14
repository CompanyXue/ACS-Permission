# -*- coding: UTF-8 -*-

class UserGroupService(object):
	
	'''
	 * 根据用户角色名查找有哪些用户
	 * @param role_name
	 * @return 
	'''
	def find_by_group_name(role_name):
		
		pass
	
	'''
	 * 插入数据到t_user_role做关联关系
	 * @param userRoles
	 * @return
	'''
	def add_user_group(users,groups):
		
		pass
	
	''' 
	 * 根据用户名查找用户拥有的组信息
	 * @param username
	 * @return Set<Role>
	'''
	def find_group_by_user_name(username):
		pass

def remove_user_from_group(user_group, users):
    
    pass
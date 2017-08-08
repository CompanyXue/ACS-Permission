# -*- coding: UTF-8 -*-

class role_group_service:
	/**
	 * 根据用户角色名查找有哪些用户
	 * @param role_name
	 * @return 
	 */
	def find_by_rolename(role_name):
	
	/**
	 * 插入数据到t_user_role做关联关系
	 * @param userRoles
	 * @return
	 */
	def add_user_roles(user_roles):
	
	/**
	 * 根据用户的id删除t_user_role表中的记录
	 * @param userId
	 * @return
	 */
	def delete_by_userid(user_id):
	
	/**
	 * 根据userId查找用户的角色信息
	 * @param userId
	 * @return
	 */
	def find_role_by_uerid(user_id):

	
	/** 
	 * 根据登录名查找用户拥有的角色信息
	 * @param username
	 * @return Set<Role>
	 */
	def find_role_by_user_name(username):
	
	/**
	 * 根据资源resourceId查找对应可访问的用户角色Role
	 * @param username
	 * @return Set<Role>
	 */
	def find_role_by_resource_id(resource_id):
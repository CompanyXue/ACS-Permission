# -*- coding: UTF-8 -*-

class ResourceService:
	'''
	 * 查询全部（门禁）资源信息
	 * @return List<Resource> 
	 '''
	def find_all_resource():

	'''
	 * 根据用户id获取该用户可访问的资源（权限）
	 * @param userId
	 * @return
	 '''
	def find_resources_by_userid(user_id):

	'''
	 * 根据角色Id获取可访问的资源（权限）
	 * @param role_group_id
	 * @return
	 '''
	def find_resources_by_roleid(role_group_id):

	'''
	 * 插入记录到t_role_resource表，建立role与resource的关联关系
	 * @param rolesResource
	 * @return
	 '''
	def add_roles_resource(roles_resource):
	
	def delete_role_resource(roles_resource):





# -*- coding: UTF-8 -*-
from database.models import  User, Role, db, Usergroup

class RoleService(object):
	
	def __init__(self, params):
		'''
		Constructor
		'''
		
# 根据用户角色名查找有哪些用户
# @param role_name
# @return 
def find_users_by_rolename(role_name):
	role = db.session.query(Role).filter(Role.name==role_name).one()
	for user in role.users:
		if user is not None:
			yield user
			# print user

'''
 * 根据用户的Id查找用户的角色信息
 * @param userId
 * @return
 '''
def find_role_by_uerid(user_id):
	user = db.session.query(User).filter(User.id==user_id).one()
	for role in user.role:
		if role is not None:
			yield role

''' 
 * 根据用户名查找用户拥有的角色信息
 * @param username
 * @return Set<Role>
 '''
def find_role_by_user_name(user_name):
	user = db.session.query(User).filter(User.name==user_name).one()
	for role in user.role:
		if role is not None:
			yield role
	pass
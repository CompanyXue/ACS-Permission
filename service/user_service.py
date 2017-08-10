# -#- coding: UTF-8 -#-

from database import models

class UserService:
	
	# 查询全部用户信息
	def find_all_users():
		users = db.session.query(User)
		for user in users:
			print user
		db.session.commit()
		pass

    
	# 根据用户名或者电话号码、组织来查询用户信息
	# @return 

    def find_user(name, phone,organization):
        sql = "select # from t_user where name==name||phone==phone||organization==organization"
        pass
	'''
	 根据用户id 查询用户信息
	  @return User

	'''
    def find_user_by_id(userid):
    	user = db.session.query(User).filter(User.id==userid).one()
		print user
    	pass

    ##
	# 更新用户信息
	#
    def update_user(_id, data):
		pass
    ##
	# （管理员）重置用户密码信息
	# @return
	
    def reset_password(User user):
    	pass
	##
	 # 修改用户密码
	 # @return
	 #/
    def update_pwd(username,pwd):
    	pass
    ##
	 # 根据角色名查询用户数量
	 # @return
	 #/
    def find_count_by_rolename(String description):
    	pass
    ##
	 # 根据组织id查询全部用户信息
	 # @return
	 #/
	def get_all_by_organization(id):
		pass
	##
	 # 设置用户所属权限组
	 # @return
	 #/
    def set_user_group(user_group_id):
		pass
    def add_users_from_group(users, user_group_id):
		pass
	def remove_user_from_group(user_group_id, users):
		pass
    

us = UserService.new()
# us.find_all_users()
us.find_user_by_id(2)
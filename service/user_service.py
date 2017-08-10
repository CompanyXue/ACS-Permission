# -*- coding: UTF-8 -*-

class UserService:
	/**
	 * 查询全部用户信息
	 */
	def find_all_users():


    /**
	 * 根据用户名或者电话号码、组织来查询用户信息
	 * @return 
	 */
    def find_user(username, phone,organization):
    	sql = "select * from t_user where name==username||phone==phone||organization==organization"
    	
	/**
	 * 根据用户id 查询用户信息
	 * @return User
	 */
    def find_user_by_id(userid):
    	

    /**
	 * 更新用户信息
	 */
    def update_user(_id, data):

    /**
	 * （管理员）重置用户密码信息
	 * @return
	 */
    def reset_password(User user):

	/**
	 * 修改用户密码
	 * @return
	 */
    def update_pwd(username,pwd):

    /**
	 * 根据角色名查询用户数量
	 * @return
	 */
    def find_count_by_rolename(String description):

    /**
	 * 根据组织id查询全部用户信息
	 * @return
	 */
	def get_all_by_organization(id):

	/**
	 * 设置用户所属权限组
	 * @return
	 */
    def set_role_group(role_group_id):

    def add_users_from_group(users, role_group_id):

	def remove_user_from_group(role_group_id, users):

    




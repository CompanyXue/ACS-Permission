# -*- coding: UTF-8 -*-

class permission:
	#数据表属性 初始化
	def __init__(self, role_name, role_type, is_activated, create_time, _id=None):
        self._id = _id
        # self.role_group_id = role_group_id  
        self.role_name = role_name
        self.role_type = role_type   #管理员与普通身份
        self.create_time = create_time
        self.is_activated = is_activated
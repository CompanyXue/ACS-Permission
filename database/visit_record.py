# -*- coding: UTF-8 -*-
class VisitRecord:
	def __init__(self, userid, user_name, role_group_id, name, start_time, event_time, _id=None):
        self._id = _id
        self.userid = userid
        self.user_name = user_name
        # self.role_group_id = role_group_id
        self.name = name  #真实姓名
        self.start_time = start_time
        self.event_time = event_time


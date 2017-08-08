# -*- coding: UTF-8 -*-

class Resource:
    #数据表属性 初始化
    def __init__(self, location, setting, organization, door_type, is_activated, state, create_time, pwd, _id=None):
        self._id = _id
        self.organization = organization
        self.setting = setting  #参数设置 
        self.location = location
        self.door_type = door_type
        self.create_time = create_time
        self.is_activated = is_activated
        self.state = state
        self.pwd = pwd

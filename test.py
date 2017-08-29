# -*- coding: UTF-8 -*-

import database
from database.config_setting import init_db, date_time
from business.user_business import UserBusiness
from services.permission_service import PermissionService

if __name__ == '__main__':
    init_db()

    users = UserBusiness.find_all_users()
    for i in users:
        print (i)

    print (date_time.strftime('%Y-%m-%d %H:%M:%S'))

    PermissionService.add_permission_by_name('baidu')

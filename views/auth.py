# -*- coding: UTF-8 -*-

from database.config_setting import app
from business.user_business import UserBusiness
from werkzeug.security import safe_str_cmp
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

class Auth(object):
    # 自动生成认证 Token
    @classmethod
    def generate_auth_token(cls, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': cls.id})
    
    # 验证 Token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = UserBusiness.find_user_by_id(data['id'])
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        user = {u.name: u for u in UserBusiness.find_all_users()}.get(username,
                                                                      None)
        if user and safe_str_cmp(user.password.encode('utf-8'),
                                 password.encode('utf-8')):
            return user
    
    @classmethod
    def identity(cls, payload):
        user_id = payload['identity']
        return {u.id: u for u in UserBusiness.find_all_users()}.get(user_id,
                                                                    None)
    
# auth = Auth()
# jwt = JWT(app, auth.authenticate, auth.identity)

'''
Flask-jwt对JWT生成和解析的过程进行了封装，所以使用时只需要调用它的接口，从上面的代码可以看到，实现代码非常简洁。

（1）错误处理

认证类的error_handler方法提供了异常处理，flask-jwt内部也封装了对异常和各类错误的处理，可以从后面运行的结果中看到。

（2）认证方法

认证类的authenticate方法提供认证服务，正确返回用户信息用作生成token的用户依据(payload)

（3）鉴权

认证类的identity用于鉴权并返回结果
'''

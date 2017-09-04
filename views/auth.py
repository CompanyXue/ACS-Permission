# -*- coding: UTF-8 -*-

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

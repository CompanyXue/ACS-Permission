# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Date, Boolean, DateTime
from database.config_setting import db, date_time


class AppCliet(db.Model):
    __tablename__ = 'appclient'

    # 表的结构:
    client_key = db.Column(db.String(40), primary_key=True)
    client_secret = db.Column(db.String(55), index=True, unique=True, nullable=False)
    user = db.relationship('User')
    name = Column(db.String(100), unique=True)
    
    # public or confidential
    is_confidential = db.Column(db.Boolean)
    
    _realms = db.Column(db.Text)
    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)
    
    description = Column(db.Text)
    create_time = Column(db.DateTime, default=date_time)
    modified_date = Column(db.DateTime, default=create_time)

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'
    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_realms(self):
        if self._realms:
            return self._realms.split()
        return []

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []

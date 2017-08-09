# -*- coding: UTF-8 -*-
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings") 

from django.db import models
from django.contrib.auth.models import Permission, User #,BaseUserManager, AbstractBaseUser

# from django.contrib import admin
# admin.site.register(BlogPost)

if django.VERSION >= (1, 7):#自动判断版本
    django.setup()

class PermissionList(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s(%s)' %(self.name,self.url)
                                              
class RoleList(models.Model):
    name = models.CharField(max_length=64)
    permission = models.ManyToManyField(PermissionList,null=True,blank=True)

    def __unicode__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(email,
            username = username,
            password = password,
        )

        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    nickname = models.CharField(max_length=64, null=True)
    sex = models.CharField(max_length=2, null=True)
    role = models.ForeignKey(RoleList,null=True,blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def has_perm(self,perm,obj=None):
        if self.is_active and self.is_superuser:
            return True

# uer = UserManager.create_user('123','hello','123456')
# print user
Permission.objects.create(name=u'权限管理',content_type_id=2,codename=u'权限管理描述')
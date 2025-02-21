from django.db import models


#管理员
class Manager(models.Model):
    ManagerID = models.AutoField('管理员ID', primary_key=True)
    ManagerPassword = models.CharField('管理员密码', max_length=255, null=False)
    ManagerName = models.CharField('管理员名称', max_length=20, null=False)


class Permission(models.Model):
    PermissionID = models.AutoField('操作权限ID', primary_key=True)
    PermissionName = models.CharField('操作权限内容', max_length=50, null=False)


class User(models.Model):
    UserID = models.AutoField("用户ID", primary_key=True)
    UserName = models.CharField('用户名', max_length=20)
    UserPassword = models.CharField('用户密码', max_length=255, null=False)
    UserPermission = models.ForeignKey('Permission', on_delete=models.SET_NULL, null=True)


class ShipOwner(models.Model):
    ShipOwnerID = models.AutoField('船东ID', primary_key=True)
    ShipOwnerName = models.CharField('船东名称', max_length=20, null=False)
    ShipOwnerContact = models.CharField('船东联系方式', max_length=30)
    ShipManagerBindingFlag = models.BooleanField('管理公司账号是否绑定用户', default=False)


class
# Create your models here.

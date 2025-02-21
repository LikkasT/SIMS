from django.db import models


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
    ShipOwnerBindingFlag = models.BooleanField('船东账号是否绑定用户', default=False)
    ShipOwnerBindingUser = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)


class ShipManager(models.Model):
    ShipManagerID = models.AutoField('管理公司ID', primary_key=True)
    ShipManagerName = models.CharField('管理公司名称', max_length=20, null=False)
    ShipManagerContact = models.CharField('管理公司联系方式', max_length=30)
    ShipManagerBindingFlag = models.BooleanField('管理公司账号是否绑定用户', default=False)
    ShipManagerBindingUser = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)


class ShipType(models.Model):
    ShipTypeID = models.AutoField('船舶类型ID', primary_key=True)
    ShipTypeName = models.CharField('船舶类型名称', max_length=30, null=False)


class Ship(models.Model):
    MMSI = models.CharField('船舶MMSI号码', max_length=9, primary_key=True)
    ShipName = models.CharField('船舶名称', max_length=30)
    IMO = models.CharField('船舶IMO号码', max_length=7, null=False)
    CallSign = models.CharField('呼号', max_length=7)
    DWT = models.DecimalField('载重吨', max_digits=10, decimal_places=2)
    NT = models.DecimalField('净吨', max_digits=10, decimal_places=2)
    GT = models.DecimalField('总吨', max_digits=10, decimal_places=2)
    ShipLength = models.DecimalField('船舶长度', max_digits=6, decimal_places=2)
    ShipWidth = models.DecimalField('船舶宽度', max_digits=6, decimal_places=2)
    ShipBuildYear = models.DateTimeField('船舶建造年份')

# Create your models here.

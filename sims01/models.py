from django.db import models
from django.contrib.gis.db import models


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


class Nation(models.Model):
    CountryCode = models.CharField('国家代码', max_length=10, primary_key=True)
    CountryName = models.CharField('国家名称', max_length=20, null=False)
    CountryEnName = models.CharField('国家英文', max_length=56, null=False)
    TimeZone = models.IntegerField('时区', null=False)


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
    ShipPic = models.ImageField('船舶图片', upload_to='static/img/ship', null=True)
    ShipBindingShipOwner = models.ForeignKey('ShipOwner', on_delete=models.SET_NULL, null=True)
    ShipBindingShipManager = models.ForeignKey('ShipManager', on_delete=models.SET_NULL, null=True)
    Type = models.ForeignKey('ShipType', on_delete=models.SET_NULL, null=True)
    FlagCountry = models.ForeignKey('Nation', on_delete=models.PROTECT, null=True)


class Province(models.Model):
    ProvinceID = models.AutoField('省份ID', primary_key=True)
    ProvinceName = models.CharField('省份名称', max_length=30, null=True)
    Belonging = models.ForeignKey('Nation', on_delete=models.CASCADE, null=True)


class PortType(models.Model):
    PortTypeID = models.AutoField('港口类型ID', primary_key=True)
    PortTypeFlag = models.IntegerField('港口类型类别', null=False)
    PortTypeMessage = models.CharField('港口类型信息', max_length=20, null=False)


class Port(models.Model):
    PortID = models.AutoField('港口ID', primary_key=True)
    PortName = models.CharField('港口名称', max_length=30, null=False)
    PortUnlocode = models.CharField('港口五字码', max_length=5, null=False)
    PortLatitude = models.DecimalField('港口中心点纬度', max_digits=9, decimal_places=6)
    PortLongitude = models.DecimalField('港口中心点经度', max_digits=9, decimal_places=6)
    PortGeom = models.GeometryField('港口范围', null=True)
    PortLevel = models.CharField('港口级别', max_length=30, null=True)
    PortUpdateTime = models.DateTimeField('港口数据更新时间', auto_now=True)
    PortDataState = models.CharField('港口数据状态', max_length=8, null=False, default='N', choices=[('NEW', 'N'), ('MODIFIED', 'M'), ('DELETED', 'D')])
    PortState = models.CharField('港口状态', max_length=10, null=False, default='F', choices=[('FREE', 'F'), ('OCCUPATION', 'O'), ('DISUSE', 'D')])
    PortEnName = models.CharField('港口英文名', max_length=60)
    PortLength = models.DecimalField('港口长', max_digits=10, decimal_places=2)
    PortWidth = models.DecimalField('港口宽', max_digits=10, decimal_places=2)
    BerthsNumber = models.IntegerField('泊位数量')
    PortBindingFlag = models.BooleanField('港口账号是否绑定用户', null=False, default=False)
    Belonging = models.ForeignKey('Province', on_delete=models.PROTECT, null=False)
    Type = models.ManyToManyField('PortType')
    PortBindingUser = models.OneToOneField('User', on_delete=models.SET_NULL, null=True)


class Berths(models.Model):
    BerthsID = models.AutoField('泊位ID', primary_key=True)
    BerthsName = models.CharField('泊位名称', max_length=30)
    BerthsEnName = models.CharField('泊位英文名', max_length=60)
    BerthCode = models.CharField('泊位代码', max_length=10, null=False)
    BerthType = models.CharField('泊位类型', max_length=30,null=True)
    BerthLon = models.DecimalField('泊位位置经度', max_digits=9, decimal_places=6)
    BerthLat = models.DecimalField('泊位位置纬度', max_digits=9, decimal_places=6)
    BerthLength = models.DecimalField('泊位长度', max_digits=6, decimal_places=2)
    BerthCapacity = models.IntegerField('泊位容量')
    DesignDepth = models.IntegerField('设计水深')
    ActualDepth = models.IntegerField('实际水深')
    TurningDepth = models.DecimalField('转船深度', max_digits=5, decimal_places=2)
    TurningArea = models.IntegerField('转船区域')
    FairwayDepth = models.IntegerField('航道水深', null=True)
    BerthMeasureDate = models.DateTimeField('泊位数据测量日期', null=True, blank=True)
    BerthRemark = models.TextField('泊位备注', null=True, blank=True)
    BerthPerimeter = models.IntegerField('泊位周长', null=True)
    BerthGeom = models.GeometryField('泊位范围', null=True, blank=True)
    LoadingFlag = models.BooleanField('到货情况', default=False)
    ProductType = models.CharField('发货类型', max_length=30, null=True)
    BerthDataUpdateTime =models.DateTimeField('泊位数据更新时间',auto_now=True)
    DeleteFlag = models.BooleanField('删除标记', default=False)
    CreateTime = models.DateTimeField('首次入库时间', null=True)
    BerthState = models.CharField('泊位状态', max_length=10, null=False, default='F', choices=[('FREE', 'F'), ('OCCUPATION', 'O'), ('DISUSE', 'D')])
    Port = models.ForeignKey('Port', on_delete=models.CASCADE, null=False)


class Moored(models.Model):
    MooredID = models.AutoField('船舶停靠ID', primary_key=True)
    Voyage = models.DecimalField('航程', max_digits=10, decimal_places=2)
    VoyageTime = models.DecimalField('航时', max_digits=10, decimal_places=2)
    BerthArriveTime = models.DateTimeField('靠泊时间', null=True, blank=True)
    BerthDepartTime = models.DateTimeField('离泊时间', null=True, blank=True)
    DepartLon = models.DecimalField('出发港离港经度', max_digits=9, decimal_places=6)
    DepartLat = models.DecimalField('出发港离港纬度', max_digits=9, decimal_places=6)
    PortArriveTime = models.DateTimeField('到达港口时间', auto_now=True)
    PortDepartTime = models.DateTimeField('离开港口时间', null=True, blank=True)
    MooredStatus = models.BooleanField('停泊状态', default=True)
    Ship = models.ForeignKey('Ship', on_delete=models.SET_NULL, null=True, blank=True)
    Berth = models.ForeignKey('Berths', on_delete=models.CASCADE, null=True, blank=True)


class Application(models.Model):
    ApplicationID = models.AutoField('申请ID', primary_key=True)
    ApplicationText = models.TextField('文字内容', null=True, blank=True)
    ApplicationPic = models.ImageField('申请图片信息', upload_to='static/img/application', null=True, blank=True)
    ApplicationFlag = models.CharField('审核结果', max_length=6, null=False, default='U', choices=[('UNREAD', 'U'), ('ADOPT', 'A'), ('REFUSE', 'R')])
    Manager = models.ForeignKey('Manager', on_delete=models.SET_NULL, null=True, blank=True)
    Permission = models.ForeignKey('Permission', on_delete=models.SET_NULL, null=True, blank=True)
    User = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    Ship = models.ForeignKey('Ship', on_delete=models.SET_NULL, null=True, blank=True)
    Port = models.ForeignKey('Port', on_delete=models.SET_NULL, null=True)
    Berths = models.ForeignKey('Berths', on_delete=models.SET_NULL, null=True, blank=True)
    Moored = models.ForeignKey('Moored', on_delete=models.SET_NULL, null=True)
# Create your models here.

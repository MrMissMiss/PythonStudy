from django.db import models


# Create your models here.
class Location_type(models.Model):
    """位置类型"""
    lt_name = models.CharField(max_length=100)


class Floor(models.Model):
    """楼层信息"""
    f_name = models.CharField(max_length=100)


class Equipment(models.Model):
    """设备信息"""
    no = models.CharField(max_length=100)  # 设备编码
    type = models.CharField(max_length=100)  # 设备类型
    name = models.CharField(max_length=100)  # 设备名称
    floor = models.ForeignKey(Floor, on_delete=models.DO_NOTHING)  # 所在楼层
    location_type = models.ForeignKey(Location_type, on_delete=models.DO_NOTHING)  # 位置类型
    location = models.CharField(max_length=100)  # 具体位置
    state = models.CharField(max_length=10)  # 设备状态
    date_create = models.DateTimeField(auto_now_add=True)  # 设备创建时间


class Record(models.Model):
    """巡检记录"""
    equip = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING)  # 设备信息-> 设备ID
    # user = models.ForeignKey(User)  # 巡检人员
    mhq_state = models.BooleanField()  # 灭火器状态
    xhs_state = models.BooleanField()  # 消火栓状态
    wg_state = models.BooleanField()  # 外观及标识状态
    date_create = models.DateTimeField(auto_now_add=True)  # 记录生成时间

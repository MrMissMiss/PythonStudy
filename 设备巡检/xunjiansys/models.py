from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import TruncTime, TruncSecond


# Create your models here.
class Location_type(models.Model):
    """位置类型"""
    lt_name = models.CharField(max_length=100, verbose_name='位置类型', )

    def __str__(self):
        """返回字符串类型"""
        return self.lt_name

    class Meta:
        verbose_name = '位置类型'
        verbose_name_plural = '位置类型'


class Floor(models.Model):
    """楼层信息"""
    f_name = models.CharField(max_length=100, verbose_name='楼层')

    def __str__(self):
        """返回字符串类型"""
        return self.f_name

    class Meta:
        verbose_name = '所在楼层'
        verbose_name_plural = '所在楼层'


class Equipment(models.Model):
    """设备信息"""
    no = models.CharField(max_length=100, verbose_name='设备编码')
    type = models.CharField(max_length=100, verbose_name='设备类型')
    name = models.CharField(max_length=100, verbose_name='设备名称')
    floor = models.ForeignKey(Floor, verbose_name='所在楼层', on_delete=models.DO_NOTHING)
    location_type = models.ForeignKey(Location_type, verbose_name='位置类型', on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100, verbose_name='具体位置')
    state = models.CharField(max_length=10, verbose_name='设备状态')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.no + ' ' + self.name

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'


class Record(models.Model):
    """巡检记录"""
    equipment = models.ForeignKey(Equipment, on_delete=models.DO_NOTHING, verbose_name='设备ID')
    users = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='巡检人员')
    mhq_state = models.BooleanField(default=True, verbose_name='灭火器状态')
    xhs_state = models.BooleanField(default=True, verbose_name='消火栓状态')
    wg_state = models.BooleanField(default=True, verbose_name='外观及标识状态')
    date_create = models.DateTimeField(auto_now_add=True)  # 记录生成时间

    def __str__(self):
        """返回模型的字符串表示"""
        return self.equipment.no + ' ' + str(self.date_create)

    class Meta:
        verbose_name = '巡检记录'
        verbose_name_plural = '巡检记录'

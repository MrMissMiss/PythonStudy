"""定义xunjiansys的URL模式"""

from django.urls import path
from . import views

urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),

    # 设备清单
    path(r'equipments/', views.equipments, name='equipments'),

    # 设备详情页
    path(r'equipments/<equipment_no>/', views.equipment_detail, name='equipment_detail'),

    # 添加新设备
    path(r'add_equipment/', views.add_equipment, name='add_equipment'),

    # 添加新巡检记录
    path(r'add_record/', views.add_record, name='add_record'),

]
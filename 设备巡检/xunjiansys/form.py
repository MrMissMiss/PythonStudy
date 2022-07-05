from django import forms
from .models import Equipment, Record, Floor, Location_type


class EquipmentForm(forms.ModelForm):
    """设备类表单"""
    class Meta:
        model = Equipment
        fields = ['no', 'type', 'name', 'floor', 'location_type', 'location', 'state']
        labels = {
            'no': '设备编号',
            'type': '设备类型',
            'name': '设备名称',
            'floor': '所属楼层',
            'location_type': '位置类型',
            'location': '详细位置',
            'state': '设备状态',
        }


class RecordForm(forms.ModelForm):
    """巡检记录表单"""
    class Meta:
        model = Record
        fields = ['equipment', 'mhq_state', 'xhs_state', 'wg_state']
        labels = {
            'equipment': '设备',
            'mhq_state': '灭火器状态',
            'xhs_state': '消火栓状态',
            'wg_state': '外观及标识状态',
        }


class FloorForm(forms.ModelForm):
    """楼层表单"""
    class Meta:
        model = Floor
        fields = ['f_name']
        labels = {'f_name': '楼层'}


class Location_typeForm(forms.ModelForm):
    """位置类型表单"""
    class Meta:
        model = Location_type
        fields = ['lt_name']
        labels = {'lt_name': '位置类型'}


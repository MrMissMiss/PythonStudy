from django import forms
from .models import Equipment, Record, Floor, Location_type


class EquipmentForm(forms.ModelForm):
    """设备类表单"""
    class Meta:
        model = Equipment
        fields = ['no', 'type', 'name', 'floor', 'location_type', 'location', 'state']
        labels = {
            'no': '',
            'type': '',
            'name': '',
            'floor': '',
            'location_type': '',
            'location': '',
            'state': '',
        }


class RecordForm(forms.ModelForm):
    """巡检记录表单"""
    class Meta:
        model = Record
        fields = ['equip', 'mhq_state', 'xhs_state', 'wg_state']
        labels = {
            'equip': '',
            'mhq_state': False,
            'xhs_state': False,
            'wg_state': False,
        }


class FloorForm(forms.ModelForm):
    """楼层表单"""
    class Meta:
        model = Floor
        fields = ['f_name']
        labels = {'f_name': ''}


class Location_typeForm(forms.ModelForm):
    """位置类型表单"""
    class Meta:
        model = Location_type
        fields = ['lt_name']
        labels = {'lt_name': ''}


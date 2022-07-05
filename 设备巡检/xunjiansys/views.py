from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
from xunjiansys.form import EquipmentForm, RecordForm
from xunjiansys.models import Equipment, Record


def index(request):
    """巡检系统主页"""
    return render(request, 'xunjiansys/index.html')


@login_required
def equipments(request):
    """设备列表页"""
    equipments = Equipment.objects.order_by('date_create')
    context = {'equipments': equipments}
    return render(request, 'xunjiansys/equipments.html', context)


@login_required
def equipment_detail(request, equipment_no):
    """显示单个设备的详细信息"""
    equipment = Equipment.objects.get(no=equipment_no)
    records = Record.objects.get(equipment=equipment)
    context = {'equipment': equipment, 'records': records}
    return render(request, 'xunjiansys/equipment_detail.html', context)


def add_equipment(request):
    """添加新设备"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = EquipmentForm()
    else:
        # POST提交的数据，对数据进行处理并保存
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('xunjiansys:equipments'))

    context = {'form': form}
    return render(request, 'xunjiansys/add_equipment.html', context)


def records(request, equipment_no):
    """显示某设备的巡检记录"""
    equipment = Equipment.objects.get(no=equipment_no)
    records = Record.objects.get(equipment=equipment)



def add_record(request, equipment_no):
    """添加新巡检记录"""
    if request.method != 'POST':
        # 创建一个空表单
        form = RecordForm()
    else:
        # 对POST提交的数据进行处理
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('xunjiansys:records'))

    context = {'form': form}
    return render(request, 'xunjiansys/add_record.html', context)



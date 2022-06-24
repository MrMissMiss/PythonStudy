from django.shortcuts import render


# Create your views here.
def index(request):
    """巡检系统主页"""
    return render(request, 'xunjiansys/index.html')


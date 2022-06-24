"""为应用程序users定义URL模式"""

from django.urls import path as url
from django.contrib.auth.views import LoginView
from django.conf.urls import include

from . import views

urlpatterns = [
    # 登录界面
    url(r'login/', LoginView.as_view(template_name='users/login.html'), name='login'),

    # 注销
    url(r'logout/', views.logout_view, name='logout'),

    # 注册
    url(r'register/', views.register, name='register'),

]
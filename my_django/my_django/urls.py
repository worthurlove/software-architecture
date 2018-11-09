"""my_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SA_test import views as SA_test_views

urlpatterns = [
    path('', SA_test_views.index,name = 'index'),  #添加的第一个视图
    # path('add/',SA_test_views.add,name='add'),#加法计算视图
    path('add/',SA_test_views.add2,name='add2'),
    path('admin/', admin.site.urls),
    path('echo', SA_test_views.echo, name='echo'),
]

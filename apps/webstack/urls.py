# -*- coding: utf-8 -*-
from django.urls import path
from .views import index_view, test_view

urlpatterns = [
    path('', index_view, name='index'),  # 主页，自然排序
    path('test/', test_view, name='test'),
]
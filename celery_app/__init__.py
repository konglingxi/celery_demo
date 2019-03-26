# -*- coding: utf-8 -*-
from celery import Celery

__author__ = 'klx'
"""
切换到celery_app模块同级目录
#A客户端命令(开始进程)：
celery worker -A celery_app -l info
#B客户端命令(开始监控)：
celery beat -A celery_app -l info
"""
"""
问题一：无法运行
1.修改配置中时区，CELERY_TIMEZONE = 'Asia/Shanghai'
2.更新celery版本为4.0.2
"""

app = Celery('demo')
# 通过 Celery 实例加载配置模块
app.config_from_object('celery_app.celeryconfig')

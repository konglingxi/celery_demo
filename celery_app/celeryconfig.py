# -*- coding: utf-8 -*-
from datetime import timedelta
from celery.schedules import crontab

__author__ = 'klx'

# 方式一
# BROKER_URL = 'redis://127.0.0.1:6379/1'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
# 方式二
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 6379
BROKER_URL = 'redis://'
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_RESULT_BACKEND_SETTINGS = {
    "host": "127.0.0.1",
    "port": 27017,
    "database": "jobs",
    "taskmeta_collection": "stock_taskmeta_collection",
}

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)
# 设置时区
CELERY_TIMEZONE = 'Asia/Shanghai'
# 添加定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',  # 任务函数
        'schedule': timedelta(seconds=2),  # 时间
        'args': (2, 8)  # 任务函数参数
    },
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=8, minute=54),
        'args': (4, 5)
    }
}

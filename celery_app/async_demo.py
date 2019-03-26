# coding:utf-8
"""
异步任务：直接运行本.py文件
"""
from celery_app.task1 import add

__author__ = 'klx'

if __name__ == '__main__':
    add.delay(1, 2)

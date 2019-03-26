# -*- coding: utf-8 -*-
import time

from celery_app import app

__author__ = 'klx'


@app.task
def multiply(x, y):
    time.sleep(4)
    return x * y

# _*_ coding=utf-8 _*_
from celery import Celery

app = Celery('tasks', broker='redis://localhost',
             backend='redis://localhost')


@app.task  # 添加装饰器生效
def add(x, y):
    print('enter call func...')
    return x + y


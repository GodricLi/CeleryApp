# _*_ coding=utf-8 _*_


from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('test',
             broker='redis://:123456@localhost:6379/2',
             backend='redis://:123456@localhost:6379/1',
             include=['celery_app.task']
             )


if __name__ == '__main__':
    app.start()

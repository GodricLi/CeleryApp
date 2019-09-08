# _*_ coding=utf-8 _*_
from celery import Celery

# celery实例
app = Celery('demo', include=['celery_app.task'])    # 添加任务
app.config_from_object('celery_app.celeryconfig')   # 加载配置

if __name__ == '__main__':
    app.start()

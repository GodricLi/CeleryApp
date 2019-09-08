# _*_ coding=utf-8 _*_

# celery配置文件

BROKER_URL = 'redis://localhost:6379/1'  # 使用redis作为消息代理

CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_app.task'
)

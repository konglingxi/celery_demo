####使用方式####
切换到celery_app模块同级目录
#A客户端命令(开始进程)：
celery worker -A celery_app -l info
#B客户端命令(开始监控)：
celery beat -A celery_app -l info
#运行异步任务,先开始进程，后运行async_demo.py
celery worker -A celery_app -l info
python async_demo.py
####ʹ�÷�ʽ####
�л���celery_appģ��ͬ��Ŀ¼
#A�ͻ�������(��ʼ����)��
celery worker -A celery_app -l info
#B�ͻ�������(��ʼ���)��
celery beat -A celery_app -l info
#�����첽����,�ȿ�ʼ���̣�������async_demo.py
celery worker -A celery_app -l info
python async_demo.py
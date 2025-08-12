broker_url = 'redis://10.195.81.63:6379/0'
result_backend = 'redis://10.195.81.63:6379/2'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True

imports = ('celery_tasks.math',)

worker_max_tasks_per_child = 100
worker_prefetch_multiplier = 1

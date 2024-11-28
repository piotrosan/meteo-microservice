import os
import sys
from celery import Celery
from pathlib import Path

root = os.path.dirname(os.path.realpath(__file__))
paths = Path(root)
sys.path.append(root)
sys.path.extend([
    f'{root}/{dir.name}' for dir in paths.iterdir() if dir.is_dir()
])

app = Celery(
    'weather_hub_ms_cron',
    broker='amqp://guest@localhost//',
    include=['weather_tasks.tasks']
)

app.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERYD_CONCURRENCY=3,
    CELERY_RESULT_SERIALIZER='json',
    CELERY_RESULT_BACKEND='mongodb://root:example@localhost:27017/?directConnection=true',
    MONGODB_SCHEDULER_URL='mongodb://root:example@localhost:27017/?directConnection=true',
    MONGODB_SCHEDULER_DB='mydb',
    MONGODB_SCHEDULER_COLLECTION="my_taskmeta_collection"
)


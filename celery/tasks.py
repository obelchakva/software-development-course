from celery import Celery
import os

REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")

broker_url = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:6379/0"
result_backend = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:6379/0"

app = Celery('tasks', broker=broker_url, backend=result_backend)

@app.task
def health_check_task():
    return "Celery worker is alive"

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, health_check_task.s(), name="health check every 60s")

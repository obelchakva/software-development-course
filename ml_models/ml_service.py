import time
import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

r = redis.Redis(host=REDIS_HOST, port=6379, password=REDIS_PASSWORD, decode_responses=True)

if __name__ == "__main__":
    print("ML service started. Waiting for tasks...")
    while True:
        # Имитация обработки задач из очереди
        task = r.lpop("ml_tasks")
        if task:
            print(f"Processing task: {task}")
            time.sleep(2)
            r.rpush("ml_results", f"processed_{task}")
        time.sleep(1)

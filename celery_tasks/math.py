import time
import random
from celery import shared_task
from celery.utils.log import get_task_logger
from app import app

logger = get_task_logger(__name__)


@app.task(bind=True)
def add(self, x, y):
    logger.info(f"Task {self.request.id} Adding {x} and {y}")
    time.sleep(random.randint(1, 5))
    logger.info(f"Task {self.request.id} Added {x} and {y}")
    return x + y


@app.task(bind=True)
def multiply(self, x, y):
    logger.info(f"Task {self.request.id} Multiplying {x} and {y}")
    time.sleep(random.randint(1, 5))
    logger.info(f"Task {self.request.id} Multiplied {x} and {y}")
    return x * y

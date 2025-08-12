from celery_tasks.math import add, multiply


result = add.delay(4, 4)
result2 = multiply.delay(4, 4)

print(result.get(timeout=10))
print(result2.get(timeout=10))

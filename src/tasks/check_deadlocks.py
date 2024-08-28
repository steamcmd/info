from main import app, logger
from celery_singleton import clear_locks


@app.task(name="check_deadlocks", bind=True)
def check_deadlocks_task(self):
    """
    If no running tasks, purge all singleton locks
    in Redis to avoid for ever deadlocks.
    """

    #active_tasks = app.tasks.keys()
    workers = app.control.inspect()
    workers = workers.active()

    total_tasks = []
    for worker in workers:
        active_tasks = workers[worker]
        for task in active_tasks:
            if task["id"] != self.request.id:
                total_tasks.append(task)

    clear_locks(app)

    logger.info("Cleared locks. No tasks were running.")

    #print(len(total_tasks))
    #print(total_tasks)

    #print(active_tasks)




    #{'celery@jona-macbook.localdomain': [{'id': '40e33378-cdcf-4008-a927-064c6fd26b0e', 'name': 'check_deadlocks', 'args': [], 'kwargs': {}, 'type': 'check_deadlocks', 'hostname': 'celery@jona-macbook.localdomain', 'time_start': 1724623549.8536904, 'acknowledged': True, 'delivery_info': {'exchange': '', 'routing_key': 'celery', 'priority': 0, 'redelivered': False}, 'worker_pid': 61992}]}
from celerydemo.celery import app

@app.task
def cus_task(*arg):
    print('This is a test task')
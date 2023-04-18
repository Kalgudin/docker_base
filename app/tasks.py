from celery import shared_task


@shared_task()
def simple_task(*args):
    summa = 0
    for arg in args:
        summa += arg
    print(summa)
    return summa

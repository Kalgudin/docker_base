from django.shortcuts import render, HttpResponse

from .tasks import simple_task


def main(request):
    # res = simple_task.delay(1, 2, 3, 4, 5)
    res =1111111111
    print(res)

    return HttpResponse(request, res)

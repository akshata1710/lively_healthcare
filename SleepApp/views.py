from datetime import timedelta, datetime
from django.shortcuts import render

from SleepApp.forms import SleeForm
from .models import Slee


def sleep(request):
    if request.GET.get("num1") and request.GET.get("num2"):
        num1 = request.GET.get("num1")
        num2 = request.GET.get("num2")

        num1 = datetime.strptime(num1, '%H:%M')

        num2 = datetime.strptime(num2, '%H:%M')

        if num2 < num1:
            nu = str(num1-num2)
            nu1 = nu.split(':')
            num = int(nu1[0])

        else:

            nu = str(num2-num1)
            nu1 = nu.split(':')

            num = int(nu1[0])

        print(num)
        print(type(num))

        day = request.GET.get("day")
        data = Slee(hours=num, days=day)
        data.save()
        fm = SleeForm()

        return render(request, "sleep.html", {"fm": fm, "msg": num})
    else:
        fm = SleeForm()
        return render(request, "sleep.html", {"fm": fm})


def index(request):
    labels = []
    data = []

    queryset = Slee.objects.all()

    for per in queryset:
        labels.append(per.days)
        data.append(per.hours)
    return render(request, 'chart.html', {
        'labels': labels,
        'data': data,
    })



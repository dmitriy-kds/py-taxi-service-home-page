from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from taxi.models import Driver, Manufacturer, Car


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_drivers": Driver.objects.all().count(),
        "num_manufacturers": Manufacturer.objects.all().count(),
        "num_cars": Car.objects.all().count(),
    }
    return render(request, "taxi/index.html", context=context)

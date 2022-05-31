from django.shortcuts import render

from cities.models import City


def home(request):
    queue_set = City.objects.all()
    context = {'object_list': queue_set}
    return render(request, 'cities/home.html', context)

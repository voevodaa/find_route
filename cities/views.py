from django.shortcuts import render

from cities.models import City


def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        context = {'object': city}
        return render(request, 'cities/detail.html', context)
    else:
        queue_set = City.objects.all()
        context = {'object_list': queue_set}
        return render(request, 'cities/home.html', context)


def main(request):
    name = 'Roman'
    return render(request, 'home.html', {'name': name})
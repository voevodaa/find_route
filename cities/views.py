from django.shortcuts import render
from django.views.generic import DetailView

from cities.models import City


def home(request, pk=None):
    #if pk:
        #city = City.objects.filter(id=pk).first()
        #context = {'object': city}
        #return render(request, 'cities/detail.html', context)
    #else:

    queue_set = City.objects.all()
    context = {'object_list': queue_set}
    return render(request, 'cities/home.html', context)


def main(request):
    name = 'Roman'
    return render(request, 'index.html', {'name': name})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

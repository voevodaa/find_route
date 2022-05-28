from django.shortcuts import render


def home(request):
    name = 'bob'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'About Us'
    return render(request, 'about.html', {'name': name})

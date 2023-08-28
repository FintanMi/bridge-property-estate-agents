from django.shortcuts import render


def index(request):
    return render(request, 'bridgeproperty/index.html')


def about(request):
    return render(request, 'bridgeproperty/about.html')

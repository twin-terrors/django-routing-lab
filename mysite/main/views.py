from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def location(request):
    return render(request, 'main/location.html')


def afisha(request):
    return render(request, 'main/afisha.html')


def collectives(request):
    return render(request, 'main/collectives.html')
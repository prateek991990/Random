from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'Generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    new = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    for i in range(length):
        new += random.choice(characters)
    return render(request, 'Generator/password.html', {'password': new})


def about(request):
    return render(request, 'Generator/about.html')

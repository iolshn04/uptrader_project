from django.shortcuts import render
from .models import Menu


def menu_view(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    return render(request, 'menu.html', {'menu': menu})
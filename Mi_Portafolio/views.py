from django.shortcuts import render
import datetime
from Projects.models import Project

now = datetime.datetime.now()
edad = now.year - 2006


def home(request):
    data = {
        'now': now,
        'edad': edad
    }

    return render(request, 'index.html', data)


def proyectos(request):
    projects = Project.objects.all()

    data = {
        'now': now,
        'projects': projects
    }

    return render(request, 'proyectos.html', data)


def contacto(request):
    data = {
        'now': now
    }

    return render(request, 'contactos.html', data)


def galeria(request):
    data = {
        'now': now
    }

    return render(request, 'galeria.html', data)

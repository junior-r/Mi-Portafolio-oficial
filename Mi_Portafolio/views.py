from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

now = datetime.datetime.now()

def home(request):
    return render(request, 'home.html', {'now': now})

def proyectos(request):
    return render(request, 'proyectos.html', {'now': now})

def contacto(request):
    return render(request, 'contactos.html', {'now': now})
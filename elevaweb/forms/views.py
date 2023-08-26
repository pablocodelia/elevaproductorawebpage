from django.shortcuts import render
from django.http import HttpResponseRedirect

from models import *
# Create your views here.


def enviar(request):
    print(request.POST)
    nombre = request.POST('nombre')
    email = request.POST('email')
    mensaje = request.POST('mensaje')
    contacto = Contacto.objects.create(
        nombre = nombre,
        email = email,
        mensaje = mensaje,
    )
    #contacto.save()
    return HttpResponseRedirect('/')

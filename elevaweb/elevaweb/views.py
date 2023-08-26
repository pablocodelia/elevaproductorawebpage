

    
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST


def blog(request):
    return render(request, 'blog.html', {})
from .models import * 

@require_POST
def enviar(request):
    try:
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')

        # Realiza la validación de los datos si es necesario

        cliente = Cliente(nombre=nombre, email=email, mensaje=mensaje)
        cliente.save()

        # Realiza cualquier acción adicional que necesites después de guardar

        return HttpResponseRedirect('/')
    except Exception as e:
        # Manejo de errores: puedes personalizar este mensaje de acuerdo a tus necesidades
        error_message = "Ha ocurrido un error durante el envío de datos."

        # Puedes imprimir el error en la consola para depuración
        print(f"Error: {str(e)}")

        # Puedes renderizar una página de error o redirigir a una página específica
        return render(request, 'error.html', {'error_message': error_message})

    # Opcionalmente, podrías también considerar un bloque finally para acciones finales
    # que siempre deben ejecutarse, independientemente de si hay un error o no.

from django.shortcuts import render, redirect
from .models import Correo  # Asumiendo que tienes un modelo llamado Correo para guardar los correos

def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Correo.objects.create(email=email)
            # Puedes realizar otras acciones aquí, como enviar un correo de confirmación, etc.
            return redirect('/')  # Redirigir a una página de éxito o a donde prefieras
    return HttpResponseRedirect('/')

def correo_exitoso(request):
    return HttpResponseRedirect('/')
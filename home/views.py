from django.shortcuts import render
from .forms import *

# Create your views here.
def informacion_vista (request):
    nombre = "Diego Prado"
    juegos = ['juego1', 'juego 2', 'juego 3']
    
    return render(request , 'info.html', locals())

def contacto_vista (request):
    bandera = True
    juegos = ['juego1', 'juego 2', 'juego 3']
    if request.method == 'POST':
        formulario = contacto_form(request.POST)
        if formulario.is_valid():
            print("xxxxxxxxxxxxxxxx")
            nom = formulario.cleaned_data['nombre']
            men = formulario.cleaned_data['mensaje']
            bandera = False
    else: #GET
        formulario = contacto_form()    
    return render(request, 'contacto.html', locals())

def principal_vista (request):
    return render(request, 'principal.html')
from django.shortcuts import render
#from django.http import HttpResponseRedirect
from .models import Client
from django.contrib.auth.models import User

# muestra todos los clientes

def index(request):
    dataClient = Client.objects.all()
    return render(request, "crear_cliente.html", { "clientes" : dataClient })


def crear_cliente(request):
    return render(request, 'gestionfinanciera/crear_cliente.html')

# se crea la funcion la cual valida la informacion que llega del formulario

'''def Client(request):
    template_name = 'crear_cliente'
    form = ClienteForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
    return HttpResponseRedirect('/')

    return render(request,template_name,{'form':form})
'''

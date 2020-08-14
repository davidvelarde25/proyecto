from django.shortcuts import render
#from django.http import HttpResponseRedirect
from .models import Client, Reference
from django.contrib.auth.models import User
from django.urls import reverse
# vistas basadas en clase
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

# muestra todos los clientes

def index(request):
    dataClient = Client.objects.all()
    return render(request, "home.html", { "clientes" : dataClient })

# clase para litar los clientes
class BadgetUpdate(UpdateView):
    model = Client
    fields = '__all__'

    def get_success_url(self):
        return reverse('')

# clase para crear los clientes
class ClientCreate(CreateView):
    model = Client
    fields = '__all__'

    def get_success_url(self):
        return  reverse('')


def crear_cliente(request):
    if request.method == "POST":
        Client.objects.create()
    return render(request, "")

# se crea la funcion la cual valida la informacion que llega del formulari

def Reference(request):
    template_name = 'crear_referencia.html'
    form = ReferenciaForm()

    if request.method ==  'POST':
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')


    return render(request, template_name, {'form':form})

from django.shortcuts import render
from aplicacion.forms import FormCliente
from aplicacion.models import Cliente
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def listadoClientes(request):
    clientes = Cliente.objects.all()
    data = {'clientes' : clientes}
    return render(request,'clientes.html',data)

def agregarClientes(request):
    form = FormCliente()
    if request.method == 'POST':
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request,'agregarClientes.html',data)

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('/clientes')

def actualizarCliente(request, id):
    cliente = Cliente.objects.get(id = id)
    form = FormCliente(instance=cliente)
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarClientes.html', data)
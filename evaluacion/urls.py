"""
URL configuration for evaluacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion.views import index, listadoClientes, agregarClientes, eliminarCliente, actualizarCliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('clientes/',listadoClientes, name='listadoClientes'),
    path('agregarClientes/',agregarClientes, name='agregarClientes'),
    path('eliminarCliente/<int:id>', eliminarCliente, name='eliminarCliente'),
    path('actualizarCliente/<int:id>', actualizarCliente, name='actualizarCliente')
]

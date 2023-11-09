from django import forms
from aplicacion.models import Cliente

class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


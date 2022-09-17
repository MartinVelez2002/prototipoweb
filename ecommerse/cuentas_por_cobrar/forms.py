from django import forms
from django.forms import ModelForm
from cuentas_por_cobrar.models import *

class PagoForm (ModelForm):
    class Meta:
        model = PagoDeuda
        fields = ['monto','fecha_registro']
        widgets = {
            'monto':forms.DecimalField(attrs={'class':'form-control','placeholder':'Ingrese el monto'}),
            'fecha_registro': forms.DateInput(format=('%d/%m/%Y'))
        }

class CalcularForm (ModelForm):
    class Meta:
        model = Interes

        fields = '__all__'
        widgets = {
            'deuda': forms.DecimalField(attrs={'class':'form-control','readonly':True}),
            'tiempCuotas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto deudor'})
        }

class CrearForm (ModelForm):
    class Meta:
        model = CrearCobro
        fields = ['deudaPer','fecha_registro']
        widgets={
            'deudaPer': forms.DecimalField(attrs={'class':'form-control'}),
            'fecha_registro': forms.DateInput(format=('%d/%m/%Y'))
        }
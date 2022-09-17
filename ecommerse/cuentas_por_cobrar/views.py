from django.shortcuts import render, HttpResponse
from django.views.generic import *
# Create your views here.
html_base = """
    <h1>Shopping Car</h1>
    <ul>
       <li><a href="/">Inicio</a></li>
       <li><a href="/articulo/">Articulos</a></li>
       <li><a href="/cliente/">Clientes</a></li>
       <li><a href="/venta/">Ventas</a></li>
       <li><a href="/consulta/">Consultas</a></li>
    </ul>
"""
#CUENTAS POR COBRAR
class CuentasCobrar (TemplateView):
    template_name = "cuentas_por_cobrar/cuentasCobrar.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Cuentas por Cobrar'
        context["nombre"]= 'CASM'
        return context

class CalculoInteres (TemplateView):
    template_name = "cuentas_por_cobrar/interés.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre"]= 'CASM'
        return context

class CobroDeuda(TemplateView):
    template_name = "cuentas_por_cobrar/cobro_deuda.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Pago de su Deuda'
        context["nombre"] = 'CASM'
        return context

class CrearCobro(TemplateView):
    template_name = "cuentas_por_cobrar/creaCobro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = 'Cuentas por Cobrar'
        context["nombre"] = 'CASM'
        return context

#FIN DE CUENTAS POR COBRAR

#PANTALLA DEL INICIO
class Inicio(TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Menu Principal"
        context['url_anterior']= '/'
        return context

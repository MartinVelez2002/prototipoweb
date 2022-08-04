from django.shortcuts import render, HttpResponse
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

def cuentasCobrar (request):
    data = {
    'titulo':'Cuentas por Cobrar',
    'nombre': 'LA MEJOR EMPRESA',
    }
    return render(request, 'cuentas_por_cobrar/cuentasCobrar.html',data)

def calculoInteres (request):
    return render(request, 'cuentas_por_cobrar/interés.html')

def pago_deuda (request):
    return render(request, 'cuentas_por_cobrar/cobro_deuda.html')

#FIN DE CUENTAS POR COBRAR


def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)

def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)
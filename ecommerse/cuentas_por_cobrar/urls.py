from django.urls import path

from cuentas_por_cobrar.views import *

app_name="cuentasCob"
urlpatterns = [
    path('cuentasCobrar', CuentasCobrar.as_view(), name='CuentasCobrar' ),
    path('calculoInteres', CalculoInteres.as_view(), name='CalculaInteres' ),
    path('cobroDeuda', CobroDeuda.as_view(), name='CobroDeuda' ),
    path('crearCobro', CrearCobro.as_view(), name='CrearCobro' ),

]
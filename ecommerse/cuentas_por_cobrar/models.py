from django.db import models

# Create your models here.

class Base(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True, auto_now=False)
    fecha_modificacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    fecha_eliminacion = models.DateTimeField(auto_now_add=False, auto_now=True)
    estado = models.BooleanField(default=True)
    class Meta:
        abstract=True

class PagoDeuda (Base):
    monto = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    class Meta:
        ordering = ('id',)
        def __str__(self):
            return "{}".format(self.monto)

class CrearCobro (Base):
    deudaPer = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    class Meta:
        ordering = ('id',)
        def __str__(self):
            return "{}".format(self.deudaPer)
class Interes (models.Model):
    deuda = models.ForeignKey(CrearCobro,on_delete=models.PROTECT,null=False, blank=False)
    tiempCuotas = models.IntegerField(default= 3)
    tasa = models.IntegerField(default=10)
    class Meta:
        ordering = ('id',)
        def __str__(self):
            return "{} - {}".format(self.deuda.deudaPer,self.tiempoCuotas)
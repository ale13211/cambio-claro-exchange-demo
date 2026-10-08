from django.db import models
class Cotizacion(models.Model):
 moneda=models.CharField(max_length=3)
 compra=models.DecimalField(max_digits=12,decimal_places=2)
 venta=models.DecimalField(max_digits=12,decimal_places=2)
 actualizada=models.DateTimeField(auto_now=True)
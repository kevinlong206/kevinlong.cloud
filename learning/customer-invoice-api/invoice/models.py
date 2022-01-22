from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Customer(models.Model):
    created = models.DateTimeField(default=timezone.now)
    name = models.TextField()

class Service(models.Model):
    name = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    price_per_unit = models.FloatField(validators=[MinValueValidator(0.0)])


class InvoiceLineItem(models.Model):
    created = models.DateTimeField(default=timezone.now)
    customer_id = models.ForeignKey('Customer', related_name='invoicelineitems',on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    units_consumed = models.FloatField(validators=[MinValueValidator(0.0)])
    unique_charge_id = models.TextField(unique=True, editable=False)



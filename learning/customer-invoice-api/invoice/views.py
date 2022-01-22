from invoice.models import Customer, Service, InvoiceLineItem
from invoice.serializers import CustomerSerializer, ServiceSerializer, InvoiceLineItemSerializer
from rest_framework import viewsets
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class InvoiceLineItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceLineItem.objects.all()
    serializer_class = InvoiceLineItemSerializer
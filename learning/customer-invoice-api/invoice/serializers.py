from rest_framework import serializers, status
from rest_framework.response import Response
from invoice.models import Customer, Service, InvoiceLineItem


class CustomerSerializer(serializers.ModelSerializer):
    invoicelineitems = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='invoicelineitem-detail',
        read_only=True
        )
    class Meta:
        model = Customer
        exclude = []

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = []




class InvoiceLineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLineItem
        exclude = []
    def validate(self, data):
        print('validating... ' + str(data))
        return data





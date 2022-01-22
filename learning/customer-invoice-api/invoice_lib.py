import requests
import json
import uuid



class InvoiceClient():
    def add_line_item(self, customer_id='', service='', units_consumed='', unique_charge_id=''):

        data = {
            "customer_id" : customer_id,
            "service": service,
            "units_consumed": units_consumed,
            "unique_charge_id": str(unique_charge_id)
        }        
        r = requests.post('http://127.0.0.1:8000/invoicelineitem/', json=data)


# Service Definitions (relates to primary key in service table)
class Services():
    GenericCompute = 1
    DataBaseHosting = 2
    IPAddress = 3
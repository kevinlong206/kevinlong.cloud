from invoice_lib import InvoiceClient, Services
import uuid


client = InvoiceClient()

r = client.add_line_item(
    customer_id=2,
    service=Services.GenericCompute,
    units_consumed=27.3,
    unique_charge_id=uuid.uuid4(),
    )

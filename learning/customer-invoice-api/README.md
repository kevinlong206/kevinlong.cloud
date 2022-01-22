
## Getting Started

#### Clone this repo:
- git clone git@github.com:zapier-interviews/interview-kevinlong206-e1b31ba15476470e8d564bcd9891b758.git zapier-billing

#### Create a new python virtual environment (only python 3 tested!):
- mkvirtualenv zapier-billing -p python3

#### Install requirements:
- cd zapier-billing
- pip install -r requirements.txt

#### Populate sample data into the dblite database
- ./manage.py migrate
- ./manage.py loaddata invoice/fixtures/fixture.yaml

#### Run the web service
- ./manage.py runserver

#### Check out the web-browseable API !
Point your browser to http://localhost:8000 and poke around

#### Add a new line item to the customer's account
Check out (or run) example_client_use.py which import invoice_lib.py

## Design Decisions
- Python 3.x
- Uses Django web framework and Django Rest Framework
- JSON for serialization
- Database is SQLite3 for ease of demonstration, very easily changeable to other relational databases with Django's ORM.

## Shortcomings
- Adds line items to 'customer' object rather than a specific invoice, assuming that the billing system would then generate invoices based on these line items 'created' date. I previously attempted to have multiple foreign key relationships between customer, service, invoice, and invoice line item, but it was getting too complex for this excericse.
- Protections against duplicate line items is done by a unique constraint using a UUID (represented as string). The client could still create duplicate charges if it sends new ones with unique UUIDs.
- API has no authentication, though this could very easily be enabled.
- No tests yet :(
- Only some edge cases for invalid data are covered, and only implicity (thanks to Djank Rest Framework's inherant serializer validations)

# Other obvious things for a production API

- API Authentication
- TLS protected HTTPs for the API
- No hardcoding of localhost URL in client library
- Way more validation, error and exception handling on webservice and client library side.


from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]


for product in products:
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8
    print('Price for sku ', product['sku'], 'is now', product['price'])

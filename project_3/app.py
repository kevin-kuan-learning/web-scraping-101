import requests
import json
from fake_useragent import UserAgent
from pprint import pprint
from urllib.parse import urljoin
import sqlite3

url = "https://www.walgreens.com/productsearch/v3/products/search"

def get_page(page):
    ua = UserAgent(verify_ssl=False)

    payload = json.dumps({
    "p": "{}".format(page),
    "s": 72,
    "view": "allView",
    "geoTargetEnabled": False,
    "abtest": [
        "tier2",
        "showNewCategories"
    ],
    "deviceType": "desktop",
    "id": [
        "350006"
    ],
    "requestType": "tier3",
    "sort": "Top Sellers",
    "couponStoreId": "15196",
    "storeId": "15196"
    })

    headers = {
    'Content-Type': 'application/json',
    'User-Agent': ua.google,
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json()

def collect(data):    
    try:
        for product in j['products']:
            prod_info = product['productInfo']
            pr = {
                'img': prod_info['imageUrl'],
                'price': prod_info['priceInfo']['regularPrice'],
                'id': prod_info['prodId'],
                'name': prod_info["productName"],
                'size': prod_info["productSize"],
                'url': urljoin(base=url, url=prod_info["productURL"]),
            }
            parsed_products.append(pr)
    except KeyError:
        pass

parsed_products = []

current_page, total_pages = 1, 99
while current_page <= total_pages:
    j = get_page(current_page)
    total_pages = int(j['summary']["totalNumPages"])
    current_page += 1
    collect(j)

connection = sqlite3.connect('project_3/product.db')
c = connection.cursor()
try:
    c.execute('''
        CREATE TABLE products (
            id TEXT PRIMATY KEY,
            name TEXT,
            url TEXT,
            size TEXT,
            price TEXT,
            image TEXT
        )
    ''')
    connection.commit()
except sqlite3.OperationalError as e:
    print(e)

for product in parsed_products:
    c.execute('''
        REPLACE INTO products (id, name, url, size, price, image) VALUES (
            ?,?,?,?,?,?
        )
    ''',
        (
            product['id'],
            product['name'],
            product['url'],
            product['size'],
            product['price'],
            product['img']
        )
    )
connection.commit()
connection.close()

pass
import requests
import json
from fake_useragent import UserAgent
from pprint import pprint
from urllib.parse import urljoin

parsed_products = []

ua = UserAgent(verify_ssl=False)
url = "https://www.walgreens.com/productsearch/v3/products/search"

payload = json.dumps({
  "p": 1,
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
  'User-Agent': ua.random,
}

response = requests.post(url, headers=headers, data=payload)

j = response.json()

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

    pprint(pr)

    parsed_products.append(pr)

pprint(parsed_products)
print(len(parsed_products))
pass
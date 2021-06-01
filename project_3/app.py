import requests
import json
from fake_useragent import UserAgent
from pprint import pprint

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
#   'Cookie': '_abck=B437AD01A0C2E3A36F0C9039A697D3B7~-1~YAAQlF9Ky68P4rB5AQAA+sa0xwUFD+u7LtyG3kL9kFX2sOfJMvE5MkHSegFn7DLWwy4f2vzA2nw+YpifqSIIOmWOakYVx491W94EWeEsW0K1yRc2OGpkbakGEgpt5nAj/SOwLgZsCX8P6WW1YKrCRwXCHASeGmXaC0SzLoMr1iCtyuGc4FnR1lwZKttoTyZlSaRZi/uHt3lVw3R/6fvu9id7r3p8CGEUMoLBYHcBPEtEwP5YbsyjunlGj9nAYn/gaavuX4UY43Yw5mYgPkOHViqi4nP8loHp9Kc0cDzMklUAVD/9wud7zRGVPt/4/u1G8yawyMz/xYHDbb6Q5qWa8u+0NRBUF6JRpsPaGFevyevbhxEgPSL1GL/9qd8=~-1~-1~-1; bm_sz=112B939D90875F071332739B93B5A345~YAAQlF9Ky64P4rB5AQAA+sa0xwvVRsNU5EYuVTunr0+LUaWjDk6E7I3qBw53ruKR5KTIzguiyLf076+I5C6nCXRHHcxjM4N1EFsppWm5YMQGBshywp6Zsu8eKWYhMns1W6IR1kOKoUAwju6a6IuGNj5W3QW0BOUlSdDAYvha7w/U2c59JAJFUCrK3FF+UjpDVaUq; akavpau_walgreens=1622553558~id=56ea1e260b198d7699367f3361daefc0'
}

response = requests.post(url, headers=headers, data=payload)

j = response.json()

pprint(j)

pass
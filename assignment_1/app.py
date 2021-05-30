import requests
from lxml import html
import json
import re

resp = requests.get('https://www.ebay.com/globaldeals', headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
})

tree = html.fromstring(resp.text)

item_info = []
item_node_list = tree.xpath("//div[@itemscope='itemscope' and @data-listing-id]")
for node in item_node_list:
    
    title = node.xpath(".//h3//span[@itemprop='name']/text()")[0]
    price = node.xpath(".//span[@itemprop='price']/text()")[0]
    url = node.xpath(".//div[@class='dne-itemtile-detail']/a[@itemprop='url']/@href")[0]
    
    if node.xpath(".//span[contains(@class, 'itemcard-hotness-red')]"):
        availability = 'AlmostGone'
    else:
        availability = 'Plentiful'

    try:
        discount_node = node.xpath(".//span[contains(@class, 'itemtile-price-bold')]/text()")[0]
        discount = re.findall(r'\d+\%', discount_node)[0]
    except IndexError:
        discount = '0%'

    item_info.append({
        'title': title,
        'price': price,
        'url': url,
        'availability': availability,
        'discount': discount
    })
    
    pass

with open('assignment_1/ebay-global-deals.json', 'w') as f:
    json.dump(item_info, f)

pass
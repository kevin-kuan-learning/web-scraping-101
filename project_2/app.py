import requests
from lxml import html

all_currencies = []
target_url_queue = ["https://coinmarketcap.com"]

def scrape_page(url):
    resp = requests.get(
        url=url,
        headers={
            'user-agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)' 
                'Chrome/73.0.3683.103 Safari/537.36'
            )
        }
    )

    tree = html.fromstring(resp.text)

    currencies = tree.xpath("//table[contains(@class, 'cmc-table')]/tbody/tr")

    for currency in currencies:
        def get(xpath_list):
            if len(xpath_list) == 0:
                return ''
            else:
                return xpath_list[0]

        try:
            name = currency.xpath(".//p[contains(@class, 'iJjGCS')]/text()")[0]
            c = {
                '_id': name,
                'Name': name,
                'Market Cap': get(currency.xpath(".//span[contains(@class, 'ftvydZ')]/text()")),
                'Price': get(currency.xpath(".//div[contains(@class, 'price___3rj7O')]/a/text()")),
                'Volume (24h)': get(currency.xpath(".//div//p[contains(@class, 'kDEzev')]/text()")),
            }
            all_currencies.append(c)
        except IndexError:
            pass

    

while len(target_url_queue) != 0:
    url = target_url_queue.pop()
    scrape_page(url)


print(len(all_currencies))

pass
import click
import json
import csv
import re
import requests
from lxml import html

def write_to_json(filename, data):
    f =  open(filename, 'w')
    json.dump(data, f)
    f.close()

def write_to_csv(filename, data):
    headers = ['title', 'price', 'in_stock', 'description']
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerow(data)

@click.command()
@click.option('--bookurl', 
    default='http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
    help='Please provide a book url to scrape from'
)
@click.option('--filename',
    default='output.json',
    help='Please provide a filename to save to'
)
def scrape(bookurl, filename):

    resp = requests.get(url=bookurl, headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    })

    tree = html.fromstring(resp.text)

    product_main = tree.xpath("//div[contains(@class, 'product_main')]")[0]
    title = product_main.xpath("./h1/text()")[0]
    price = product_main.xpath("./node()[@class='price_color']/text()")[0].strip()
    availability = product_main.xpath("./node()[contains(@class, 'availability')]/text()")[1].strip()
    description = product_main.xpath("//div[@id='product_description']/following-sibling::p[1]/text()")[0]

    in_stock = re.search(r'(\d+)', availability).group(1)

    book_information = {
        'title': title,
        'price': price,
        'in_stock': in_stock,
        'description': description
    }

    write_to_json(filename, book_information)
    extension = filename.split('.')[1]
    if extension == 'json':
        write_to_json(filename, book_information)
    elif extension == 'csv':
        write_to_csv(filename, book_information)
    else:
        click.echo("The extension you provided is invalid. Please use 'csv' or 'json'")
    
if __name__ == '__main__':
    scrape()
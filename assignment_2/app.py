import requests
from lxml import html
import re
from urllib.parse import urljoin

all_movies = []
target_urls = ['https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc&ref_=adv_prv']

def scrape_page(url):

    resp = requests.get(
        url=url,
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }
    )

    tree = html.fromstring(resp.text)

    movies = tree.xpath("//div[contains(@class, 'lister-item-content')]")

    for movie in movies:
        def get(ls):
            try:
                return ls[0]
            except IndexError:
                return ''

        def get_int(ls):
            try:
                return re.findall(r'\d+', get(ls))[0]
            except IndexError:
                return ''

        m = {
            'title': get(movie.xpath("./h3/a/text()")),
            'year_of_release': get_int(movie.xpath("./h3/span[contains(@class, 'lister-item-year')]/text()")),
            'duration': get_int(movie.xpath(".//span[contains(@class, 'runtime')]/text()")),
            'rating': get(movie.xpath(".//div[contains(@class, 'ratings-imdb-rating')]/strong/text()")),
        }

        all_movies.append(m)

    try:
        target_urls.append(
            urljoin(
                base=url,
                url=tree.xpath("//a[contains(@class, 'next-page')]/@href")[0]
            )
        )
    except IndexError:
        pass

while len(target_urls) > 0:
    scrape_page(target_urls.pop())

print(all_movies)
print(len(all_movies))

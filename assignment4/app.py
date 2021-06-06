import requests
from lxml import html
import json
import argparse


def scrape(url):

    upcoming_flights = []

    splash_url = 'http://localhost:8050/run' # not https, append /run

    lua = r'''
    splash:set_custom_headers({
        ['Cookie'] = 'w_locale=en_US'
    })
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(1))
    return splash:html()
    '''

    resp = requests.post(splash_url,json={
        'lua_source': lua,
        'url': url
    })

    print(resp.text)
    pass

    tree = html.fromstring(resp.text)
    for node_flight in tree.xpath("//div[@id='flightPageActivityLog']//div[@class='flightPageDataTable'][1]//div[contains(@class,'flightPageDataRowTall')]"):
        def get(list_of_strings):
            try:
                return list_of_strings[0].strip()
            except IndexError as e:
                raise e
        
        flight = {
            'Aircraft': get(node_flight.xpath('./div[4]/span/text()')),
            'Arrival Airport': get(node_flight.xpath("./div[3]//div[@class='flightPageActivityLogDataPart']/span[2]/text()")),
            'Arrival time': get(node_flight.xpath("./div[3]//div[@class='flightPageActivityLogDataPart']/span[1]//span/text()")).replace('\xa0', ' '),
            'Date': "{} {}".format(
                get(node_flight.xpath("./div[1]//em/text()[1]")),
                get(node_flight.xpath("./div[1]//em/text()[2]"))
            ),
            'Departure Airport': get(node_flight.xpath("./div[2]//div[@class='flightPageActivityLogDataPart']/span[2]/text()")),
            'Departure Time': get(node_flight.xpath("./div[2]//div[@class='flightPageActivityLogDataPart']/span[1]//span/text()")).replace('\xa0', ' '),
            'Duration': get(node_flight.xpath("./div[5]/em/text()")),
        }
        print(flight)
        upcoming_flights.append(flight)

    return upcoming_flights


def output(dict_list):
    print(len(dict_list))
    with open('assignment4/upcoming_flights.txt', 'w') as f:
        for u in dict_list:
            json.dump(u, f, indent='    ')
            f.write('\n')

    with open('assignment4/upcoming_flights.json', 'w') as f:
        json.dump(dict_list, f, indent='    ')

def get_flightcode():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--flightcode',
        default='JBU1623'
    )

    args = parser.parse_args()
    print(args.flightcode)

    return args.flightcode

if __name__ == '__main__':
    flightcode = get_flightcode()
    upcoming_flights = scrape('https://flightaware.com/live/flight/{}'.format(flightcode))
    output(upcoming_flights)
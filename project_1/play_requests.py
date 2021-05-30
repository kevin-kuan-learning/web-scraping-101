import requests

URL_OK = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
URL_NO = 'http://booxks.toscrxape.com/cataxlogue/a-lightx-in-the-attic_1000/index.html'

resp = requests.get(url=URL_OK, headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
})
resp2 = requests.get(url=URL_OK)

# input()
# print(resp)

# input()
# print(resp2)


# input()
# print(resp.text)
# input()
# print(resp.content)

# input()
print(resp.headers)

input('----------')
print(resp.request.headers)
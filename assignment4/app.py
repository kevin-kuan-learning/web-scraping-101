import requests
from lxml import html

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
    'url': 'https://flightaware.com/live/flight/JBU1623'
})

print(resp.text)
pass
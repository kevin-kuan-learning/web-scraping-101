function main(splash, args)
    headers = {
      ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
      -- ['Accept-Language'] = 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7'
      ['Accept-Language'] = 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7'
    --   ['Cookie'] = 'w_locale=en_US'
    }
    splash:set_custom_headers(headers)
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    
    local entries = splash:history()
    local last_entry = entries[#entries]
    
    return {
      html = splash:html(),
      png = splash:png(),
      har = splash:har(),
      headers = last_entry.request.headers
    }
  end
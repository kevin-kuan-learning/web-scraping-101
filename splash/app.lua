function main(splash, args)
    -- splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
  
    headers = {
      ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    splash:set_custom_headers(headers)
    
    assert(splash:go(args.url))
    assert(splash:wait(1))
    input = assert(splash:select("input[name='q']"))
  
    input:focus()
    input:send_text("My User Agent")
    -- input:send_keys("<Enter>")
  
    button = splash:select_all("input[name='btnK']")[2]
    assert(button:mouse_click())
    assert(splash:wait(1))
  
    --splash:set_viewport_full()
  
    return {
      png = splash:png(),
      html = splash:html(),
      history = splash:history(),
    }
  
  end
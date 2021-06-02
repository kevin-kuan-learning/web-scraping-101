function main(splash, args)

    assert(splash:go(args.url))
    assert(splash:wait(1))
    input = assert(splash:select("input[name='q']"))
    
    input:focus()
    input:send_text("My User Agent")
    -- input:send_keys("<Enter>")

    button = splash:select_all("input[name='btnK']")[2]
    assert(button.mouse_click())
    assert(splash:wait(1))

    splash:set_viewport_full()
    
    return {
      png = splash:png(),
      html = splash:html(),
    }
  
  end
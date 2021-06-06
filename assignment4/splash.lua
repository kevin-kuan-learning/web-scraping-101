function main(splash, args)
  
  splash:set_custom_headers({
    ['Cookie'] = 'w_locale=en_US',
    ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
  })
  splash.private_mode_enabled = false
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  splash:set_viewport_full()
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
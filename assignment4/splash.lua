function main(splash, args)
  
  splash:set_custom_headers({
    ['Cookie'] = 'w_locale=en_US'
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
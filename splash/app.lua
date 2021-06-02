function main(splash, args)

    assert(splash:go(args.url))
    assert(splash:wait(1))
    return {
        png = splash:png(),
        html = splash:html(),
    }

end
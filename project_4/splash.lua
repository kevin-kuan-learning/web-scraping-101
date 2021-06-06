function main(splash, args)
  
    headers = {
      ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
      ['cookie'] = 'AKAM_CLIENTID=a6b215fabfdb5b566d52e1b846808283; gb_lang=en; gb_pipeline=GB; _gcl_au=1.1.35893563.1622816128; aff_mss_info_bak={"bak":"bak"}; reffer_channel=; landingUrl=https://www.gearbest.com/flash-sale.html; gb_countryCode=TW; gb_currencyCode=USD; gb_vsign=61c9510315826f6d3f8999ab0abab5e3bf789917; _ga=GA1.2.705318877.1622816129; _fbp=fb.1.1622816129044.789165652; globalegrow_user_id=fdda4824-9597-ab26-9f0f-b00209affd55; od=bvvffxwgfznc1622816133056; osr_landing=https://www.gearbest.com/flash-sale.html; osr_referrer=originalurl; _gid=GA1.2.35557613.1622950837; gb_fcm=2; gb_fcmPipeLine=GB; cdn_countryCode=TW; AKA_A2=A; WEBF_guid=a6b215fabfdb5b566d52e1b846808283_1622954268; WEBF_predate=1622954268; _uetsid=f4868770c67811eb8de125537085248b; _uetvid=5088a3e0c53f11ebb102930abd6571b2; globalegrowbigdata2018_globalegrow_session_id_0f03c390-7e85-a18e-a8bc-c827b3a7b1bd=false; globalegrowbigdata2018_globalegrow_session_id=0f03c390-7e85-a18e-a8bc-c827b3a7b1bd; gb_pf={"rp":"originalurl","lp":"https://www.gearbest.com/flash-sale.html","wt":1622954269552}; gb_userinfo=eyJ1c2VyIjp7InVzZXJOYW1lIjoiIiwiZW1haWwiOiIiLCJhdmF0YXIiOiIiLCJpc05ld1VzZXIiOjAsInVzZXJJZCI6IjAifSwiY29sbGVjdCI6MCwiY2FydENvdW50IjowLCJpc0xvZ2luIjpmYWxzZSwidGlja2V0Q291bnQiOjAsInNpdGVNZXNzYWdlVGltZUludGVydmFsIjowfQ==; gb_soa_www_session=eyJpdiI6Iko5cTJTZHUrXC9sSDUyK0VxRkVlSml3PT0iLCJ2YWx1ZSI6IlFqK3NmNldCaUExdnVOaGpGNTBZbEhvM2JiY1BPRmIwb0trdk5wSzhiWHV0OXBqOWdIeGJtMmtVelViNCtGcGNFWGVcL0N5cmE1azdIRkVjUGp4MUpZdz09IiwibWFjIjoiMTEyYmZiODVjYzAyOTU0MjZlYjc4ZWE2NWI5MTQ3NDMzNDEyM2IxNGFjZDI1NDJmMWZmOTlhMGNmMjViNjE1NCJ9'
    }
    splash:set_custom_headers(headers)
    splash.private_mode_enabled = false
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    
    -- splash:set_viewport_full()
    
    
    return {
      html = splash:html(),
      png = splash:png(),
      har = splash:har(),
    }
  end
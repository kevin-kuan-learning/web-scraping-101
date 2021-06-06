from lxml import etree

input('--------------ETREE-----------------')

tree = etree.parse("fundamentals/src/web_page.html")
s = etree.tostring(tree)

title_element = tree.find('head/title')
print(title_element.text)

paragraph_element = tree.find('body/p')
print(paragraph_element.text)

list_items = tree.findall('body/ul/li')
print(list_items)
for li in list_items:
    a = li.find('a')
    if a is not None:
        print('{} {}'.format(li.text.strip(), a.text))
    else:
        print(li.text)

input('--------------XPATH-----------------')


# if we were to use etree all the way, we have to use absolute paths from <html> tag
# we will use xpath next to search for any level

paragraph_text = tree.xpath('//body/p/text()')[0]
print(paragraph_text)

list_items = tree.xpath('//li')
for li in list_items:
    # text = li.xpath('//text()') # this does not work. we still get the text of all html code
    text = ''.join(map(str.strip, li.xpath('.//text()')))
    print(text)

pass


input('--------------CSS-------------------')

html = tree.getroot()
print(html)
title_element = html.cssselect('title')[0]
print(title_element.text)

paragraph = html.cssselect('p')[0]
print(paragraph.text)

list_items = html.cssselect('li')
for li in list_items:
    a = li.cssselect('a')
    if len(a) == 0:
        print(li.text)
    else:
        print('{} {}'.format(li.text.strip(), a[0].text))

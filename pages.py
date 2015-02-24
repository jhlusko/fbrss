import os

f = open("pages.html")
text = f.read()
f.close()

p = open("prefix.txt")
prefix = p.read()
p.close()

pages = open("pages.opml", mode='w')
pages.write(prefix)

i = 0
while text.find('HREF="', i) > 0:
    firstquote = text.find('HREF="', i)
    secondquote = text.find('"', firstquote + 6)
    url = text[firstquote+6:secondquote]
    print("URL: " + url)
    thirdquote = text.find('">', secondquote)
    secondbracket = text.find("<", thirdquote+2)
    name =text[thirdquote+2:secondbracket]
    print("Name: " + name)
    firstquote = text.find('HREF="', secondbracket)
    secondquote = text.find('.xml', firstquote + 6)
    feed = text[firstquote+6:secondquote+4]
    print("Feed: "+feed)
    pages.write('''<outline type="rss" text="%s" title="%s" xmlUrl="%s" htmlUrl="%s"/>''' % (name, name, feed, url))
    pages.write("\n \n")
    i = secondquote
    print i

pages.write("</outline></body></opml>")
pages.close()

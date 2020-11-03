import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')

print('Retrieving: %s' % link)

html = urllib.request.urlopen(link, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

sum = 0

for tag in tags:
    sum += int(tag.contents[0])

print(sum)

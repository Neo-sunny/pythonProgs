import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


#Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter- ")
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('a')
for tag in tags:
    print("Tag: ", tag)
    print("URL: ", tag.get('href', None))
    print('Contents: ', tag.contents[0])
    print('Attrs: ', tag.attrs)
import urllib.request, urllib.parse, urllib.error
import re

url = input('Enter url -')
html=urllib.request.urlopen(url).read()
links=re.findall(b'href="(http://.*?)"',html)
#The b prefix does nothing in 2.x, but tells the 2to3 script 
#not to convert it to a Unicode string in 3.x.
for link in links:
    print(link.decode())
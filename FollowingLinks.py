import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


#Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

pageCount=1    
def followLink(url):
    html=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html, 'html.parser')   
    count=0
    tags=soup('a')
    for tag in tags:
        count=count+1
        if count==18:
            URL=tag.get('href', None)
            print(URL)
            print('Contents: ', tag.contents[0])
            return URL
            
url=input("Enter- ")         
newUrl=followLink(url)    
while(pageCount<7):
    newUrl=followLink(newUrl)  
    pageCount=pageCount+1
    
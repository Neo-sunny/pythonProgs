import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

#Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
sum=0
address = input('Enter location: ')
url = urlopen(address,context=ctx).read()
data=url.decode()
info = json.loads(data)
lists=info["comments"]
for countVal in lists:
    value=countVal["count"]    
    sum=sum+value
print(sum)    

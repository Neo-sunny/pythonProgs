import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

sum=0
    #Ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
address = input('Enter location: ')
url = urlopen(address,context=ctx).read()
data=url.decode()
tree = ET.fromstring(data)
lst_comm = tree.findall('comments/comment')
    #print(lst_comm)
for comm in lst_comm:
    val=comm.find('count').text
    sum=sum+int(val)
print(sum)        
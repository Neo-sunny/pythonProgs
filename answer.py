import re

txt=' <Hi  this>  Hello  <how are you>'
txt1='this is a [sample] string with [some] special words. [another one]'

re1='.*?'	# Non-greedy match on filler
re2='(<[^>]+>)'	# Tag 1
re3='.*?'	# Non-greedy match on filler
re4='(<[^>]+>)'	# Tag 2
lst=txt.split()
lst1=txt1.split('\[(.*?)\]')
print(lst,lst1)
print(len(lst))
rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    tag1=m.group(1)
    tag2=m.group(2)
    print ("("+tag1+")"+"("+tag2+")"+"\n")

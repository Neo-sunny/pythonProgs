import re

hand=open('/Users/Neo/Downloads/python/regex_sum_5536.txt') 
sum=0;
for line in hand:
    line=line.strip();
    y=re.findall('[0-9]+', line)
    if y:
        for i in y:
            val=int(i)
            sum=sum+val
print(sum)            



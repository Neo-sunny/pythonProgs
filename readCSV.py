import csv

#%precision 2

with open('/Users/Neo/Desktop/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
print(mpg[:3] )# The first three dictionaries in our list.

print(sum(float(d['cty']) for d in mpg) / len(mpg))
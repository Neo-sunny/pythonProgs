#!/usr/bin/env python  

# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
# 
# ---------------------------------------------------------------

import sys            

for line in sys.stdin:  
    line = line.strip()  
    keys = line.split()  #split line at blanks (by default) and return a list of keys
    for key in keys:    
        value = 1        
        print('{0}\t{1}'.format(key, value) ) 
#the {} is replaced by 0th,1st items in format list
#also, note that the Hadoop default is 'tab' separates key from the value


#!/usr/bin/env python

# ---------------------------------------------------------------
#This reducer code will input a line of text and 
#    output <word, total-count>
# ---------------------------------------------------------------
import sys

last_key      = None           
running_total = 0

for input_line in sys.stdin:
    input_line = input_line.strip()
    this_key, value = input_line.split("\t", 1)
    value = int(value)  #int() will convert a string to integer (no error checking)
 
    # ---------------------------------
    #    if this current key is same 
    #          as the last one Consolidate
    #    otherwise  Emit
    # ---------------------------------
    if last_key == this_key:                            
        running_total += value  
    else:
        if last_key:            
        
            print( "{0}\t{1}".format(last_key, running_total) )
                                
        running_total = value    #reset values
        last_key = this_key
#if this key that was just read in is different, and the previous (ie last) key is not empty,
#   then output  the previous <key running-count>
if last_key == this_key:
    print( "{0}\t{1}".format(last_key, running_total)) 
	
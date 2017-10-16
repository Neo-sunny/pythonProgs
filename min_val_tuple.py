def min_steps(step_records):
    """ Random """
    tmp=list()
    for k,v in step_records.items():
        tmp.append((v,k))
    print( tmp)
    tmp.sort()
    print(tmp)
    print(min(tmp))        

step_records = [('2010-01-01':1),
                ('2010-01-02':2),
                ('2010-01-03':3)]
                
min_steps(step_records)                    
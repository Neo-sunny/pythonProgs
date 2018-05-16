def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    max_val = 0;
    max_key = ''
    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        
    # enter code here
    for word in word_list:
        for letter in word:
            letter_count[letter] = letter_count.get(letter, 0)+1
            
    for k,v in letter_count.items():
        if max_val < v:
            max_val = v
            max_key = k
    print(max_val,max_key)
    #print(letter_count)
    v=list(letter_count.values())
    k=list(letter_count.keys())
    print(v)
    print(max(v))
    print(v.index(max(v)))
    print(k)
    print(k[v.index(max(v))])
        
    
count_letters("listen stransge womens lyinsg in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony".split());

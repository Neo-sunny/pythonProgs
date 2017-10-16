inp=input("Enter String ")
prev=ord(inp[0])
str1=inp[0]
str=inp[1:]
for i in str:
    curr=ord(i)
    if prev==curr:
        str1=str1+i
    elif prev!=curr:
        print(str1,end=" ")
        prev=curr
        str1=""
        str1=i        
print(str1)
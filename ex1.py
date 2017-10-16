
sum=0
count=0
average=0
while True:
        inp=input("Enter a number: ")
        if(inp=='done'):
            break
        try:
            val=int(inp)	
            sum=sum+val
            count=count+1
        except:        
            print("Invalid Input")           
          
average=sum/count
print(sum, count, average)    
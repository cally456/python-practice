
n = int(input("Enter the number"))
idx=2
while(idx<(int(n**5)+1)):
    if(n%idx)==0:
        print("not a prime")
        break
    idx +=1;
else:
    print("Prime:")
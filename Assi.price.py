price=int(input("Enter the price of bike:"))
if(int(price>100000)):
   print(price+0.2*price+1.5*price, "is total amount")
    
elif(int(price in range(100000,50000))):
    print(price+0.8*price+0.1*price,"is total amount")

elif(int(price in range(50000,40000))):
    print(price+0.5*price+0.5*price,"is total amount")
    

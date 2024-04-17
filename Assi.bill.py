units=int(input("Enter the units of electricity of bill:"))

if(units in range(1,101)):
    print("no charge")
elif(units in range(101,201)):
    bill=units*5
    print(bill)
elif(units in range(201,1000)):
    bill=units*10
    print(bill)
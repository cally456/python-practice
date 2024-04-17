num=int(input("Enter the number:"))
if(num%400==0) and (num%100==0):
    print("Year is leap year")
elif(num%4==0) or (num%100!=0):
    print("Year is leap year")
else:
    print("year is not leap  ")
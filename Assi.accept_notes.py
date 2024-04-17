# accept amount from user and find the minimum number notes required to get the amount amount =512  

notes=[2000,500,200,100,50,20,10,5,2,1]
amount =int(input("Enter Amount to be paid:"))

for C in notes:
    count =amount//C
    print("Notes Value:",C,"\t number of notes",count)
    amount =amount%C

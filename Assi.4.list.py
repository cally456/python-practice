# alist=[100, 200, 300, 400, 500]
# print(alist[-1:-6:-1])
#2
# no=int(input("Enter the number"))
# l1=list(no for no in range(150,251) if no%4==0)
# l2=(l1)

# print(l2)

#3
# aList = [1, 4, 9, 16, 25, 36, 49] 
# for i in range(0,len(aList)):
#     aList[i]=int(aList[i]**0.5)
# print(aList)
#4
# list1 = [5, 6,7]
# list2 = [0, 1] 
# l3=[]
# for num1 in list1:
#     for num2 in list2:

#         print(f"{num1}{num2}", end=",")

#5
# list1 =[10,20,30,40]
# list2=[100,200,300,400]

# reversed_list2 = list2[::-1]

# for item1,item2 in zip(list1,reversed_list2):
#     print(item1,item2)

#6
# l1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
# for i in l1:
#     if(i==""):
#         l1.remove(i)
# print(l1)

#7
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#8
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# subList = ["h", "i", "j"]
# list1[2][1][2].extend(subList)
# print(list1)

#9
# list1 = [5, 10, 15, 20, 25, 50, 20]

# # Iterate through the list
# for index, value in enumerate(list1):
#     # Check if the current value is 20
#     if value == 20:
#         # Replace the value with 200
#         list1[index] = 200
#         # Break the loop after updating the first occurrence
#         break

# # Print the modified list
# print(list1)
#10
# list1 = [5, 20, 15, 20, 25, 50, 20]
# list1 =[value for value in list1 if value !=20]

# print(list1)

#11
no=int(input("Enter the number:"))

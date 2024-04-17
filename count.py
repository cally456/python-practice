num=100
num_str = str(num)
print("Count of digits is ",len(num_str))
sum_digits=0
for c in num_str:
    digit = int(c)
#     print(digit)
    sum_digits = sum_digits + digit
print("Sum of digits is ", sum_digits)
# Given a string in format Emp_name:Emp_id
# If emp_is is perfect square -- > Print only vowels from emp_name
# Else if emp_id is prime -- > print alternate characters from emp_name
# Else if emp_id is odd -- > print sum of ascii values of characters in emp_name
# Else print None

employ_data="John:4"
emp_name,emp_id= employ_data.split(':')
if int(emp_id)**0.5:
    vowels=""
    for char in emp_name:
        if char.lower() in'aeiou':
            vowels +=char
    print(vowels)

elif int(emp_id) > 1:
    is_prime = True
    for i in range(2, int(emp_id) // 2 + 1):
        if int(emp_id) % i == 0:
            is_prime = False
            break
    if is_prime:
        # If emp_id is prime, print alternate characters from emp_name
        alternate_chars = ""
        for i in range(len(emp_name)):
            if i % 2 == 0:
                alternate_chars += emp_name[i]
        print(alternate_chars)
# Check if emp_id is odd
if int(emp_id) % 2 != 0:
    # If emp_id is odd, print sum of ASCII values of characters in emp_name
    ascii_sum = 0
    for char in emp_name:
        ascii_sum += ord(char)
    print(ascii_sum)

# If none of the conditions are met, print None
else:
    print("None")
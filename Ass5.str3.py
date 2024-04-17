# Find all overlapping occurrences of given substring in given string
# Ex.
# String = 0111
# Substring = 11
# Expected answer : 2
# String : ANANAAAANNN
# Substring: ANA
# Expected answer : 2
# String : ANANAAAANNN
# Substring: AA
# Expected answer : 3

str1="ANANANAN"
str2="ANAN"
idx=0
count =0
while idx < len(str1):
    if str1[idx : idx+len(str2)] == str2:
        count+=1
    idx+=1
print(count)
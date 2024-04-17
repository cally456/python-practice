#  create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1
# and second last char of s2, and so on. Any leftover chars go at the end of the result.
# Given:
# s1 = "Abc"
# s2 = "Xyz"
# output::
# AzbycX

s1 = "Abc"
s2 = "Xyz"

# Initialize empty string to store the result
result = ""

# Initialize two pointers for iterating through both strings
i = 0
j = len(s2) - 1

# Iterate through both strings simultaneously
while i < len(s1) and j >= 0:
    # Add characters from s1 and s2 alternatively
    result += s1[i] + s2[j]
    # Move the pointers
    i += 1
    j -= 1

# Add any leftover characters from s1, if any
result += s1[i:]

# Add any leftover characters from s2, if any
result += s2[:j+1]

print(result)
#  Count occurrence of spaces, and special characters in given string
# Ex.
# Input: Fgh^f #89
# Expected output :
# Spaces: 1
# Special characters: 2

input_str= "Fgh^f #89"
space_count =0
special_count=0
for char in input_str:
  if char == '':
    space_count +=1 
  elif not char.isalnum():
    special_count +=1

print("Spaces:",space_count)
print("Special character:",special_count)
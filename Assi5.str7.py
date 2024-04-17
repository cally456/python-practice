# prompt: Input= “this is a good number 9089786756 and 8900000000 is a desired number”

import re

input_string = "this is a good number 9089786756 and 8900000000 is a desired number"

# Find all numeric strings using regular expressions
numeric_strings = re.findall(r'\d+', input_string)

# Convert numeric strings to integers
numeric_values = [int(num) for num in numeric_strings]

# Print the numeric values
print(numeric_values)

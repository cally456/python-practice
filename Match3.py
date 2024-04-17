n = int(input("Enter the number of lines (odd number): "))

# Calculate the number of lines in the upper half and the lower half
half_lines = n // 2

# Print the upper half of the diamond, including the middle line
for i in range(half_lines + 1):
    spaces = i
    stars = n - 2 * i
    print(" " * spaces + "*" * stars)

# Print the lower half of the diamond
for i in range(half_lines - 1, -1, -1):
    spaces = i
    stars = n - 2 * i
    print(" " * spaces + "*" * stars)
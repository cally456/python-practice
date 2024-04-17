list_1 = ['apple', 'cherry', 'mango']

# Flag
is_item_present = False

for item in list_1:
    if len(item) == 3:
        is_item_present = True
        break

if is_item_present:
    print('Item with length 3 is found.')
else:
    print('Item with length 3 is NOT found.')
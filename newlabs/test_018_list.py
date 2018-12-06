#!/usr/bin/env python3

# The JOIN method on a list... combines the elements of the list
list1 = ['ZZ', 'YY', 'XX', 'WW', 'VV' ]
print("list1: ", list1)

# Places a comma between the list items
sep_string = ","
s1 = sep_string.join(list1)
print("s1: ", s1)

# Place a comma and a space, between the list items
sep_string = ","
s2 = sep_string.join(list1)
print("s2: ", s2)

# Places a dash between the list items
sep_string = "_"
s3 = sep_string.join(list1)
print("s3: ", s3)